"""
frontend/streamlit_app.py
---------------------------
This frontend NEVER imports Mysql or touches taskmanager.db directly.
Every single action here goes through `requests` calling the FastAPI
backend over HTTP -- exactly like Postman does, exactly like a React
app would. That separation is what the assignment means by "the UI
must not access SQLite directly": the backend is the only thing
allowed to touch the database; the frontend is just another client.

st.session_state is Streamlit's way of remembering values (like the
JWT token) between reruns -- Streamlit re-runs this whole script top
to bottom on every click, so without session_state you'd lose the
token the instant you clicked a button.
"""

import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="Task Manager v2", layout="wide")

# ---------- session state setup ----------
if "token" not in st.session_state:
    st.session_state.token = None
if "refresh_token" not in st.session_state:
    st.session_state.refresh_token = None
if "user" not in st.session_state:
    st.session_state.user = None


# def auth_headers():
#     return {"Authorization": f"Bearer {st.session_state.token}"}


def refresh_access_token():
    refresh = st.session_state.get("refresh_token")

    if not refresh:
        return False

    try:
        response = requests.post(
            f"{API_URL}/auth/refresh",
            params={"refresh_token": refresh},
            timeout=10,
        )

        if response.status_code != 200:
            return False

        data = response.json()
        new_access = data.get("access_token")

        if not new_access:
            return False

        st.session_state.token = new_access
        return True

    except requests.RequestException:
        return False


def api_request(method, path, **kwargs):
    if not st.session_state.token:
        return None

    headers = kwargs.pop("headers", {})
    headers = dict(headers)

    headers["Authorization"] = (
        f"Bearer {st.session_state.token}"
    )

    try:
        response = requests.request(
            method,
            f"{API_URL}{path}",
            headers=headers,
            timeout=10,
            **kwargs,
        )

        if response.status_code != 401:
            return response

        # Access token may have expired. Try refreshing once.
        if not refresh_access_token():
            st.session_state.token = None
            st.session_state.refresh_token = None
            st.session_state.user = None
            return response

        # Retry the original request once with the new token.
        retry_response = requests.request(
            method,
            f"{API_URL}{path}",
            headers=headers,
            timeout=10,
            **kwargs,
        )

        if retry_response.status_code == 401:
            st.session_state.token = None
            st.session_state.refresh_token = None
            st.session_state.user = None
            st.rerun()

        return retry_response

    except requests.RequestException as e:
        st.error(f"API connection error: {e}")
        return None
    
    
# ---------- LOGIN / REGISTER SCREEN ----------
def login_register_screen():
    st.title("Task Manager - Login")

    tab_login, tab_register = st.tabs(["Login", "Register"])

    with tab_login:
        email = st.text_input("Email", key="login_email")
        password = st.text_input("Password", type="password", key="login_password")
        if st.button("Login"):
            # OAuth2PasswordRequestForm on the backend expects form data,
            # not JSON -- so we send `data=`, not `json=`, here.
            response = requests.post(
                f"{API_URL}/auth/login",
                data={"username": email, "password": password},
            )
            if response.status_code == 200:
                data = response.json()

                st.session_state.token = data["access_token"]
                st.session_state.refresh_token = data.get(
                    "refresh_token"
                )

                me = api_request(
                    "GET",
                    "/auth/current-user"
                )

                if me is not None and me.status_code == 200:
                    st.session_state.user = me.json()
                    st.rerun()
                else:
                    st.session_state.token = None
                    st.session_state.refresh_token = None
                    st.error("Could not load your user profile.")
            else:
                st.error(response.json().get("detail", "Login failed"))

    with tab_register:
        name = st.text_input("Name", key="reg_name")
        reg_email = st.text_input("Email", key="reg_email")
        reg_password = st.text_input("Password", type="password", key="reg_password")
        if st.button("Register"):
            response = requests.post(
                f"{API_URL}/auth/register",
                json={"name": name, "email": reg_email, "password": reg_password},
            )
            if response.status_code == 201:
                st.success("Account created. Please log in from the Login tab.")
            else:
                st.error(response.json().get("detail", "Registration failed"))


# ---------- MAIN APP (after login) ----------
def main_app():
    st.sidebar.write(f"Logged in as **{st.session_state.user['name']}**")
    if st.sidebar.button("Logout"):
        st.session_state.token = None
        st.session_state.refresh_token = None
        st.session_state.user = None
        st.rerun()

    page = st.sidebar.radio("Go to", ["Dashboard", "Projects", "Tasks"])

    projects_resp = api_request("GET","/projects/")

    projects = (
        projects_resp.json()
        if projects_resp is not None
        and projects_resp.status_code == 200
        else []
    )

    if page == "Dashboard":
        show_dashboard(projects)
    elif page == "Projects":
        show_projects(projects)
    elif page == "Tasks":
        show_tasks(projects)


def show_dashboard(projects):
    st.title("Dashboard")

    tasks_resp = api_request(
        "GET",
        "/tasks/",
        params={"limit": 100}
    )

    tasks = (
        tasks_resp.json()
        if tasks_resp is not None
        and tasks_resp.status_code == 200
        else []
    )
    col1, col2, col3 = st.columns(3)
    col1.metric("Projects", len(projects))
    col2.metric("Total Tasks", len(tasks))
    col3.metric("Done", len([t for t in tasks if t["status"] == "done"]))


def show_projects(projects):
    st.title("Projects")

    with st.expander("Create a new project"):
        name = st.text_input("Project name")
        description = st.text_area("Description")
        if st.button("Create Project"):
            response = api_request(
                "POST",
                "/projects/",
                json={
                    "name": name,
                    "description": description
                }
            )

            if response is not None and response.status_code == 201:
                st.success("Project created.")
                st.rerun()
            else:
                st.error(
                    response.json().get("detail", "Could not create project")
                    if response is not None
                    else "Could not connect to the backend."
                )

    for project in projects:
        with st.container(border=True):
            st.subheader(project["name"])
            st.write(project["description"] or "_No description_")
            if st.button("Delete", key=f"del_project_{project['id']}"):
                response = api_request(
                    "DELETE",
                    f"/projects/{project['id']}"
                )

                if response is not None and response.status_code in (200, 204):
                    st.success("Project deleted.")
                    st.rerun()
                else:
                    st.error("Could not delete project.")


def show_tasks(projects):
    st.title("Tasks")

    if not projects:
        st.info("Create a project first before adding tasks.")
        return

    project_lookup = {p["name"]: p["id"] for p in projects}

    with st.expander("Create a new task"):
        project_name = st.selectbox("Project", list(project_lookup.keys()))
        title = st.text_input("Task title")
        description = st.text_area("Task description")
        status = st.selectbox("Status", ["pending", "in_progress", "done"])
        priority = st.selectbox("Priority", ["low", "medium", "high"])
        if st.button("Create Task"):
            response = api_request(
                "POST",
                "/tasks/",
                json={
                    "title": title,
                    "description": description,
                    "status": status,
                    "priority": priority,
                    "project_id": project_lookup[project_name],
                },
            )

            if response is not None and response.status_code == 201:
                st.success("Task created.")
                st.rerun()
            else:
                st.error(
                    response.json().get("detail", "Could not create task")
                    if response is not None
                    else "Could not connect to the backend."
                )

    st.divider()
    st.subheader("Filter tasks")
    fcol1, fcol2, fcol3 = st.columns(3)
    filter_status = fcol1.selectbox("Status filter", ["(any)", "pending", "in_progress", "done"])
    filter_priority = fcol2.selectbox("Priority filter", ["(any)", "low", "medium", "high"])
    search = fcol3.text_input("Search title")

    params = {"limit": 100}
    if filter_status != "(any)":
        params["status"] = filter_status
    if filter_priority != "(any)":
        params["priority"] = filter_priority
    if search:
        params["search"] = search

    tasks_resp = api_request(
        "GET",
        "/tasks/",
        params=params
    )

    tasks = (
        tasks_resp.json()
        if tasks_resp is not None
        and tasks_resp.status_code == 200
        else []
    )

    for task in tasks:
        with st.container(border=True):
            cols = st.columns([3, 1, 1, 1])
            cols[0].write(f"**{task['title']}**  \n{task['description'] or ''}")
            cols[1].write(task["status"])
            cols[2].write(task["priority"])
            if cols[3].button("Delete", key=f"del_task_{task['id']}"):
                response = api_request(
                    "DELETE",
                    f"/tasks/{task['id']}"
                )

                if response is not None and response.status_code in (200, 204):
                    st.success("Task deleted.")
                    st.rerun()
                else:
                    st.error("Could not delete task.")


# ---------- ENTRY POINT ----------
if st.session_state.token is None:
    login_register_screen()
else:
    main_app()
