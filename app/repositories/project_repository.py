from abc import ABC, abstractmethod

from sqlalchemy.orm import Session

from app.models.project import Project
from app.schemas.project import ProjectCreate, ProjectUpdate


class ProjectRepository(ABC):
    @abstractmethod
    def get_all(self, *, owner_id: int) -> list[Project]:
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, project_id: int) -> Project | None:
        raise NotImplementedError

    @abstractmethod
    def create(self, payload: ProjectCreate, *, owner_id: int) -> Project:
        raise NotImplementedError

    @abstractmethod
    def update(self, project: Project, payload: ProjectUpdate) -> Project:
        raise NotImplementedError

    @abstractmethod
    def delete(self, project: Project) -> None:
        raise NotImplementedError


class SQLAlchemyProjectRepository(ProjectRepository):
    def __init__(self, db: Session):
        self.db = db

    def get_all(self, *, owner_id: int) -> list[Project]:
        return (
            self.db.query(Project)
            .filter(Project.owner_id == owner_id)
            .all()
        )

    def get_by_id(self, project_id: int) -> Project | None:
        return self.db.query(Project).filter(Project.id == project_id).first()

    def create(self, payload: ProjectCreate, *, owner_id: int) -> Project:
        project = Project(
            name=payload.name,
            description=payload.description,
            owner_id=owner_id,
        )
        self.db.add(project)
        self.db.commit()
        self.db.refresh(project)
        return project

    def update(self, project: Project, payload: ProjectUpdate) -> Project:
        project.name = payload.name
        project.description = payload.description
        self.db.commit()
        self.db.refresh(project)
        return project

    def delete(self, project: Project) -> None:
        self.db.delete(project)
        self.db.commit()