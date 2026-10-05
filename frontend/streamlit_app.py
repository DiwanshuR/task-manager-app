import os

import requests
import streamlit as st


API_URL = os.getenv("API_URL", "http://127.0.0.1:8000").rstrip("/")
REQUEST_TIMEOUT = 10
TASK_PAGE_SIZE = 20

st.set_page_config(
    page_title="Task Manager",
    page_icon="◆",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ---------------------------------------------------------------------------
# Design tokens
#
# A quiet, paper-and-ink palette instead of a bright SaaS look: warm ivory
# background, navy ink for structure, a single brass accent used sparingly.
# Serif for headings (the "ledger" voice), a plain sans for everything you
# read quickly — inputs, buttons, body text.
# ---------------------------------------------------------------------------

APP_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Lora:wght@500;600;700&family=Inter:wght@400;500;600&display=swap');

:root {
    --color-bg: #FAF8F3;
    --color-surface: #FFFFFF;
    --color-ink: #23282F;
    --color-ink-muted: #6B7280;
    --color-navy: #1E3A5F;
    --color-navy-dark: #14263D;
    --color-brass: #A9812F;
    --color-brass-soft: #F1E8D5;
    --color-border: #E4DFD1;
    --color-success: #2F6846;
    --color-success-soft: #E7F0EA;
    --color-danger: #A13D3D;
    --color-danger-soft: #F5E7E5;
    --font-serif: 'Lora', Georgia, serif;
    --font-sans: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
}

html, body, [class*="css"] { font-family: var(--font-sans); color: var(--color-ink); }

.stApp { background: var(--color-bg); }

.main .block-container { max-width: 1180px; padding-top: 2.2rem; padding-bottom: 3rem; }

/* Headings use the serif voice */
h1, h2, h3, [data-testid="stHeading"] h1, [data-testid="stHeading"] h2, [data-testid="stHeading"] h3 {
    font-family: var(--font-serif);
    color: var(--color-navy-dark);
    font-weight: 600;
    letter-spacing: 0.1px;
}
[data-testid="stCaptionContainer"] { color: var(--color-ink-muted); font-size: 0.92rem; }

/* Sidebar */
[data-testid="stSidebar"] {
    background: var(--color-surface);
    border-right: 1px solid var(--color-border);
}
[data-testid="stSidebar"] .block-container { padding-top: 1.6rem; }

/* Buttons */
.stButton > button, [data-testid="stFormSubmitButton"] > button {
    min-height: 2.6rem;
    border-radius: 4px;
    font-weight: 600;
    font-family: var(--font-sans);
    border: 1px solid var(--color-border);
    background: var(--color-surface);
    color: var(--color-navy-dark);
    transition: border-color 0.15s ease, color 0.15s ease;
}
.stButton > button:hover, [data-testid="stFormSubmitButton"] > button:hover {
    border-color: var(--color-brass);
    color: var(--color-brass);
}
.stButton > button[kind="primary"], [data-testid="stFormSubmitButton"] > button[kind="primary"] {
    background: var(--color-navy);
    border-color: var(--color-navy);
    color: #FFFFFF;
}
.stButton > button[kind="primary"]:hover, [data-testid="stFormSubmitButton"] > button[kind="primary"]:hover {
    background: var(--color-navy-dark);
    border-color: var(--color-navy-dark);
    color: #FFFFFF;
}

/* Inputs */
[data-testid="stTextInput"] input,
[data-testid="stTextArea"] textarea,
[data-testid="stNumberInput"] input,
[data-testid="stSelectbox"] div[data-baseweb="select"] > div {
    border-radius: 4px;
    border: 1px solid var(--color-border);
    font-family: var(--font-sans);
}
[data-testid="stTextInput"] input:focus,
[data-testid="stTextArea"] textarea:focus {
    border-color: var(--color-navy);
    box-shadow: 0 0 0 1px var(--color-navy);
}

/* Cards / bordered containers */
[data-testid="stVerticalBlockBorderWrapper"] {
    border-color: var(--color-border) !important;
    border-radius: 6px;
    background: var(--color-surface);
}

/* Tabs */
[data-testid="stTabs"] button { font-family: var(--font-sans); font-weight: 600; color: var(--color-ink-muted); }
[data-testid="stTabs"] button[aria-selected="true"] { color: var(--color-navy-dark); }
[data-testid="stTabs"] [data-baseweb="tab-highlight"] { background-color: var(--color-brass); }

/* Metrics */
[data-testid="stMetric"] {
    background: var(--color-surface);
    border: 1px solid var(--color-border);
    border-radius: 6px;
    padding: 1rem 1.1rem;
}
[data-testid="stMetricValue"] { font-family: var(--font-serif); color: var(--color-navy-dark); }
[data-testid="stMetricLabel"] { color: var(--color-ink-muted); font-weight: 500; }

/* Dividers */
hr { border-color: var(--color-border) !important; }

/* Expanders */
[data-testid="stExpander"] { border: 1px solid var(--color-border); border-radius: 6px; }

/* Tag chips used for status / priority */
.tm-chip {
    display: inline-block;
    padding: 0.15rem 0.6rem;
    border-radius: 3px;
    font-size: 0.8rem;
    font-weight: 600;
    font-family: var(--font-sans);
    border: 1px solid transparent;
}
.tm-chip-pending   { background: var(--color-brass-soft); color: var(--color-brass); border-color: #E4D3A5; }
.tm-chip-in_progress { background: #E7EEF5; color: var(--color-navy); border-color: #C7D6E5; }
.tm-chip-done       { background: var(--color-success-soft); color: var(--color-success); border-color: #C7DECC; }
.tm-chip-low        { background: #F1F1EE; color: var(--color-ink-muted); border-color: var(--color-border); }
.tm-chip-medium     { background: var(--color-brass-soft); color: var(--color-brass); border-color: #E4D3A5; }
.tm-chip-high       { background: var(--color-danger-soft); color: var(--color-danger); border-color: #E3C5C3; }

.tm-row { padding: 0.55rem 0; border-bottom: 1px solid var(--color-border); }
.tm-row:last-child { border-bottom: none; }
.tm-mark {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    width: 2.1rem;
    height: 2.1rem;
    border: 1px solid var(--color-navy);
    color: var(--color-navy);
    font-family: var(--font-serif);
    font-weight: 600;
    border-radius: 4px;
}
</style>
"""

st.markdown(APP_CSS, unsafe_allow_html=True)

STATUS_LABEL = {"pending": "Pending", "in_progress": "In progress", "done": "Done"}
PRIORITY_LABEL = {"low": "Low", "medium": "Medium", "high": "High"}


def chip(kind: str, value: str) -> str:
    label = STATUS_LABEL.get(value, value) if kind == "status" else PRIORITY_LABEL.get(value, value)
    return f'<span class="tm-chip tm-chip-{value}">{label}</span>'


def brand_mark(letter: str = "T") -> str:
    return f'<span class="tm-mark">{letter}</span>'


# ---------- Session state ----------

for key, default in {
    "token": None,
    "refresh_token": None,
    "user": None,
}.items():
    if key not in st.session_state:
        st.session_state[key] = default


def clear_session():
    st.session_state.token = None
    st.session_state.refresh_token = None
    st.session_state.user = None


def response_error(response, fallback):
    """Return a useful message from a FastAPI error response."""
    if response is None:
        return "Could not connect to the backend. Check that FastAPI is running."

    try:
        detail = response.json().get("detail")
        if isinstance(detail, str):
            return detail
        if detail:
            return str(detail)
    except (ValueError, requests.RequestException):
        pass

    return fallback


def refresh_access_token():
    refresh = st.session_state.refresh_token
    if not refresh:
        return False

    try:
        response = requests.post(
            f"{API_URL}/auth/refresh",
            params={"refresh_token": refresh},
            timeout=REQUEST_TIMEOUT,
        )
        if response.status_code != 200:
            return False

        new_token = response.json().get("access_token")
        if not new_token:
            return False

        st.session_state.token = new_token
        return True
    except (requests.RequestException, ValueError):
        return False


def api_request(method, path, **kwargs):
    """Call the backend and try once to refresh an expired access token."""
    token = st.session_state.token
    if not token:
        return None

    headers = dict(kwargs.pop("headers", {}))
    headers["Authorization"] = f"Bearer {token}"

    try:
        response = requests.request(
            method,
            f"{API_URL}{path}",
            headers=headers,
            timeout=REQUEST_TIMEOUT,
            **kwargs,
        )

        if response.status_code != 401:
            return response

        if not refresh_access_token():
            clear_session()
            st.rerun()

        headers["Authorization"] = f"Bearer {st.session_state.token}"
        response = requests.request(
            method,
            f"{API_URL}{path}",
            headers=headers,
            timeout=REQUEST_TIMEOUT,
            **kwargs,
        )

        if response.status_code == 401:
            clear_session()
            st.rerun()

        return response
    except requests.RequestException as exc:
        st.error(f"Backend connection error: {exc}")
        return None


def show_page_title(title, description=None):
    st.title(title)
    if description:
        st.caption(description)


# ---------- Login and registration ----------

def login_register_screen():
    st.markdown(
        """
        <style>
        [data-testid="stSidebar"] { display: none; }
        .main .block-container { max-width: 1080px; padding-top: 3.5vh; }
        .tm-hero {
            background: var(--color-navy);
            border-radius: 8px;
            padding: 2.6rem 2.2rem;
            height: 100%;
            color: #F5F2EA;
        }
        .tm-hero h2 {
            color: #FFFFFF !important;
            font-size: 1.9rem;
            margin: 1.1rem 0 0.6rem;
        }
        .tm-hero p { color: #C9D3DE; line-height: 1.6; }
        .tm-hero-point {
            border-top: 1px solid rgba(255,255,255,0.15);
            padding: 0.85rem 0;
            color: #E7EAEF;
            font-size: 0.95rem;
        }
        @media (max-width: 768px) {
            .main .block-container { padding: 1rem; }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    left, right = st.columns([1, 1.15], gap="large")

    with left:
        st.markdown(
            f"""
            <div class="tm-hero">
                {brand_mark()}
                <h2>A clear place for the work you owe.</h2>
                <p>Projects, tasks and their status, kept in one ledger
                instead of scattered across chats and sticky notes.</p>
                <div class="tm-hero-point">Every task belongs to a project, and every project to someone.</div>
                <div class="tm-hero-point">Filter by status, priority or project when the list gets long.</div>
                <div class="tm-hero-point">Nothing is hidden — see what's due, what's done, what's next.</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with right:
        with st.container(border=True):
            st.markdown(
                "<div style='padding:0.4rem 0.2rem 0.8rem'>"
                "<h1 style='margin-bottom:0.2rem'>Task Manager</h1>"
                "<p style='color:var(--color-ink-muted); margin:0'>Sign in to continue.</p>"
                "</div>",
                unsafe_allow_html=True,
            )

            login_tab, register_tab = st.tabs(["Sign in", "Create account"])

            with login_tab:
                with st.form("login_form"):
                    email = st.text_input("Email", key="login_email")
                    password = st.text_input(
                        "Password",
                        type="password",
                        key="login_password",
                    )
                    submitted = st.form_submit_button(
                        "Sign in",
                        type="primary",
                        use_container_width=True,
                    )

                if submitted:
                    if not email.strip() or not password:
                        st.warning("Enter your email and password.")
                    else:
                        with st.spinner("Signing in…"):
                            try:
                                response = requests.post(
                                    f"{API_URL}/auth/login",
                                    data={
                                        "username": email.strip(),
                                        "password": password,
                                    },
                                    timeout=REQUEST_TIMEOUT,
                                )

                                if response.status_code == 200:
                                    data = response.json()
                                    st.session_state.token = data["access_token"]
                                    st.session_state.refresh_token = data.get(
                                        "refresh_token"
                                    )

                                    me = api_request("GET", "/auth/current-user")
                                    if me is not None and me.status_code == 200:
                                        st.session_state.user = me.json()
                                        st.rerun()

                                    clear_session()
                                    st.error("Could not load your user profile.")
                                else:
                                    st.error(
                                        response_error(response, "Sign-in failed.")
                                    )
                            except (requests.RequestException, ValueError, KeyError) as exc:
                                st.error(f"Could not sign in: {exc}")

            with register_tab:
                with st.form("register_form"):
                    name = st.text_input("Name", key="register_name")
                    register_email = st.text_input(
                        "Email",
                        key="register_email",
                    )
                    register_password = st.text_input(
                        "Password",
                        type="password",
                        key="register_password",
                    )
                    submitted = st.form_submit_button(
                        "Create account",
                        type="primary",
                        use_container_width=True,
                    )

                if submitted:
                    if (
                        not name.strip()
                        or not register_email.strip()
                        or not register_password
                    ):
                        st.warning("Complete all fields.")
                    else:
                        with st.spinner("Creating your account…"):
                            try:
                                response = requests.post(
                                    f"{API_URL}/auth/register",
                                    json={
                                        "name": name.strip(),
                                        "email": register_email.strip(),
                                        "password": register_password,
                                    },
                                    timeout=REQUEST_TIMEOUT,
                                )

                                if response.status_code == 201:
                                    st.success("Account created. You can now sign in.")
                                else:
                                    st.error(
                                        response_error(
                                            response,
                                            "Registration failed.",
                                        )
                                    )
                            except requests.RequestException as exc:
                                st.error(f"Could not register: {exc}")

            st.caption("Your account gives you access to your projects and tasks.")


# ---------- Projects ----------

def show_projects(projects, can_create):
    show_page_title("Projects", "Create, review and update your projects.")

    if can_create:
        with st.expander("Create a project", expanded=not projects):
            with st.form("create_project_form"):
                name = st.text_input("Project name")
                description = st.text_area("Description")
                submitted = st.form_submit_button(
                    "Create project",
                    type="primary",
                )

            if submitted:
                if not name.strip():
                    st.warning("Enter a project name.")
                else:
                    response = api_request(
                        "POST",
                        "/projects/",
                        json={
                            "name": name.strip(),
                            "description": description.strip(),
                        },
                    )
                    if response is not None and response.status_code == 201:
                        st.success("Project created.")
                        st.rerun()
                    else:
                        st.error(response_error(response, "Could not create project."))
    else:
        st.info("Your account can view projects but cannot create them.")

    if not projects:
        st.info("No projects yet. Create your first one above to start adding tasks.")
        return

    st.markdown(
        f"<p style='color:var(--color-ink-muted); margin-bottom:0.6rem'>"
        f"{len(projects)} project(s)</p>",
        unsafe_allow_html=True,
    )

    for project in projects:
        with st.container(border=True):
            header_col, mark_col = st.columns([6, 1])
            header_col.markdown(
                f"<h3 style='margin-bottom:0.1rem'>{project['name']}</h3>",
                unsafe_allow_html=True,
            )
            st.write(project.get("description") or "_No description provided._")

            with st.expander("Edit project"):
                with st.form(f"edit_project_{project['id']}"):
                    edited_name = st.text_input(
                        "Project name",
                        value=project["name"],
                        key=f"project_name_{project['id']}",
                    )
                    edited_description = st.text_area(
                        "Description",
                        value=project.get("description") or "",
                        key=f"project_description_{project['id']}",
                    )
                    save = st.form_submit_button("Save changes")

                if save:
                    if not edited_name.strip():
                        st.warning("Enter a project name.")
                    else:
                        response = api_request(
                            "PUT",
                            f"/projects/{project['id']}",
                            json={
                                "name": edited_name.strip(),
                                "description": edited_description.strip(),
                            },
                        )
                        if response is not None and response.status_code == 200:
                            st.success("Project updated.")
                            st.rerun()
                        else:
                            st.error(
                                response_error(response, "Could not update project.")
                            )

            if st.button(
                "Delete project",
                key=f"delete_project_{project['id']}",
            ):
                response = api_request("DELETE", f"/projects/{project['id']}")
                if response is not None and response.status_code in (200, 204):
                    st.success("Project deleted.")
                    st.rerun()
                else:
                    st.error(response_error(response, "Could not delete project."))


# ---------- Tasks ----------

def show_tasks(projects):
    show_page_title(
        "Tasks",
        "Filter your tasks, update their details, or create a new task.",
    )

    if not projects:
        st.info("Create a project before adding tasks.")
        return

    project_by_name = {project["name"]: project for project in projects}
    project_names = list(project_by_name)

    with st.expander("Create a task"):
        with st.form("create_task_form"):
            project_name = st.selectbox("Project", project_names)
            title = st.text_input("Task title")
            description = st.text_area("Description")
            status_col, priority_col = st.columns(2)
            status = status_col.selectbox("Status", ["pending", "in_progress", "done"])
            priority = priority_col.selectbox("Priority", ["low", "medium", "high"])
            submitted = st.form_submit_button("Create task", type="primary")

        if submitted:
            if not title.strip():
                st.warning("Enter a task title.")
            else:
                response = api_request(
                    "POST",
                    "/tasks/",
                    json={
                        "title": title.strip(),
                        "description": description.strip(),
                        "status": status,
                        "priority": priority,
                        "project_id": project_by_name[project_name]["id"],
                    },
                )
                if response is not None and response.status_code == 201:
                    st.success("Task created.")
                    st.rerun()
                else:
                    st.error(response_error(response, "Could not create task."))

    st.divider()

    with st.container(border=True):
        st.markdown(
            "<p style='font-weight:600; color:var(--color-navy-dark); margin-bottom:0.4rem'>"
            "Find tasks</p>",
            unsafe_allow_html=True,
        )
        filter_col1, filter_col2, filter_col3 = st.columns([1, 1, 2])
        status_filter = filter_col1.selectbox(
            "Status",
            ["Any status", "pending", "in_progress", "done"],
        )
        priority_filter = filter_col2.selectbox(
            "Priority",
            ["Any priority", "low", "medium", "high"],
        )
        search = filter_col3.text_input("Search by title")

        page = st.number_input(
            "Page",
            min_value=1,
            value=1,
            step=1,
            help=f"Showing up to {TASK_PAGE_SIZE} tasks per page.",
        )

    params = {
        "skip": (int(page) - 1) * TASK_PAGE_SIZE,
        "limit": TASK_PAGE_SIZE,
    }
    if status_filter != "Any status":
        params["status"] = status_filter
    if priority_filter != "Any priority":
        params["priority"] = priority_filter
    if search.strip():
        params["search"] = search.strip()

    with st.spinner("Loading tasks…"):
        response = api_request("GET", "/tasks/", params=params)
    if response is None:
        return
    if response.status_code != 200:
        st.error(response_error(response, "Could not load tasks."))
        return

    tasks = response.json()
    if not tasks:
        st.info("No tasks match these filters. Try clearing a filter or creating a new task above.")
        return

    st.caption(f"{len(tasks)} task(s) on this page")

    for task in tasks:
        with st.container(border=True):
            task_col, status_col, priority_col = st.columns([3, 1, 1])
            task_col.markdown(f"**{task['title']}**")
            task_col.caption(task.get("description") or "No description")
            task_col.caption(
                f"Project: {next((p['name'] for p in projects if p['id'] == task['project_id']), 'Unknown')}"
            )
            status_col.markdown(chip("status", task["status"]), unsafe_allow_html=True)
            priority_col.markdown(chip("priority", task["priority"]), unsafe_allow_html=True)

            with st.expander("Edit task"):
                with st.form(f"edit_task_{task['id']}"):
                    edited_title = st.text_input(
                        "Task title",
                        value=task["title"],
                        key=f"task_title_{task['id']}",
                    )
                    edited_description = st.text_area(
                        "Description",
                        value=task.get("description") or "",
                        key=f"task_description_{task['id']}",
                    )
                    edited_status = st.selectbox(
                        "Status",
                        ["pending", "in_progress", "done"],
                        index=["pending", "in_progress", "done"].index(task["status"]),
                        key=f"task_status_{task['id']}",
                    )
                    edited_priority = st.selectbox(
                        "Priority",
                        ["low", "medium", "high"],
                        index=["low", "medium", "high"].index(task["priority"]),
                        key=f"task_priority_{task['id']}",
                    )
                    edited_project = st.selectbox(
                        "Project",
                        project_names,
                        index=project_names.index(
                            next(
                                (
                                    p["name"]
                                    for p in projects
                                    if p["id"] == task["project_id"]
                                ),
                                project_names[0],
                            )
                        ),
                        key=f"task_project_{task['id']}",
                    )
                    save = st.form_submit_button("Save changes")

                if save:
                    if not edited_title.strip():
                        st.warning("Enter a task title.")
                    else:
                        response = api_request(
                            "PUT",
                            f"/tasks/{task['id']}",
                            json={
                                "title": edited_title.strip(),
                                "description": edited_description.strip(),
                                "status": edited_status,
                                "priority": edited_priority,
                                "project_id": project_by_name[edited_project]["id"],
                            },
                        )
                        if response is not None and response.status_code == 200:
                            st.success("Task updated.")
                            st.rerun()
                        else:
                            st.error(
                                response_error(response, "Could not update task.")
                            )

            if st.button("Delete task", key=f"delete_task_{task['id']}"):
                response = api_request("DELETE", f"/tasks/{task['id']}")
                if response is not None and response.status_code in (200, 204):
                    st.success("Task deleted.")
                    st.rerun()
                else:
                    st.error(response_error(response, "Could not delete task."))


# ---------- Dashboard ----------

def show_dashboard(projects):
    show_page_title("Overview", "A quick look at your projects and recent tasks.")

    with st.spinner("Loading your overview…"):
        response = api_request("GET", "/tasks/", params={"skip": 0, "limit": 100})
    if response is None:
        return
    if response.status_code != 200:
        st.error(response_error(response, "Could not load dashboard tasks."))
        return

    tasks = response.json()
    done_count = sum(1 for task in tasks if task["status"] == "done")
    open_count = len(tasks) - done_count

    metric1, metric2, metric3 = st.columns(3)
    metric1.metric("Projects", len(projects))
    metric2.metric("Tasks loaded", len(tasks))
    metric3.metric("Completed", done_count)

    if len(tasks) == 100:
        st.caption("Figures use the first 100 tasks returned by the API.")

    st.divider()
    st.subheader("Recent tasks")

    if not tasks:
        st.info("No tasks yet. Head to the Tasks page to create one.")
        return

    with st.container(border=True):
        rows = "".join(
            f"""
            <div class="tm-row" style="display:flex; align-items:center; justify-content:space-between; gap:1rem;">
                <div style="flex:1; min-width:0;">
                    <div style="font-weight:600;">{task['title']}</div>
                    <div style="color:var(--color-ink-muted); font-size:0.85rem;">
                        {task.get('description') or 'No description'}
                    </div>
                </div>
                <div>{chip('status', task['status'])}</div>
                <div>{chip('priority', task['priority'])}</div>
            </div>
            """
            for task in tasks[:8]
        )
        st.markdown(rows, unsafe_allow_html=True)


# ---------- Main app ----------

def main_app():
    user = st.session_state.user or {}
    role = user.get("role", "member")

    with st.sidebar:
        st.markdown(
            f"""
            <div style='display:flex; align-items:center; gap:0.6rem; margin-bottom:0.3rem;'>
                {brand_mark()}
                <div>
                    <div style='font-family:var(--font-serif); font-weight:600; font-size:1.1rem;
                                color:var(--color-navy-dark);'>Task Manager</div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.caption(f"Signed in as {user.get('name', 'User')} · {role.replace('_', ' ').title()}")
        st.divider()

        page = st.radio(
            "Workspace",
            ["Overview", "Projects", "Tasks"],
            label_visibility="collapsed",
        )

        st.divider()
        if st.button("Sign out", use_container_width=True):
            clear_session()
            st.rerun()

    with st.spinner("Loading your projects…"):
        projects_response = api_request("GET", "/projects/")
    if projects_response is None:
        return
    if projects_response.status_code != 200:
        st.error(response_error(projects_response, "Could not load projects."))
        return

    projects = projects_response.json()
    can_create_projects = role in ("admin", "manager")

    if page == "Overview":
        show_dashboard(projects)
    elif page == "Projects":
        show_projects(projects, can_create_projects)
    else:
        show_tasks(projects)


if st.session_state.token is None:
    login_register_screen()
else:
    main_app()