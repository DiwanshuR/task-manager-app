from abc import ABC, abstractmethod

from sqlalchemy.orm import Session

from app.models.project import Project
from app.schemas.project import ProjectCreate, ProjectUpdate
from app.models.user import User, UserRole
from sqlalchemy import or_


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict

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
mutants_xǁSQLAlchemyProjectRepositoryǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁSQLAlchemyProjectRepositoryǁget_all__mutmut: MutantDict = {}  # type: ignore
mutants_xǁSQLAlchemyProjectRepositoryǁget_by_id__mutmut: MutantDict = {}  # type: ignore
mutants_xǁSQLAlchemyProjectRepositoryǁget_visible_to_user__mutmut: MutantDict = {}  # type: ignore
mutants_xǁSQLAlchemyProjectRepositoryǁcreate__mutmut: MutantDict = {}  # type: ignore
mutants_xǁSQLAlchemyProjectRepositoryǁupdate__mutmut: MutantDict = {}  # type: ignore
mutants_xǁSQLAlchemyProjectRepositoryǁdelete__mutmut: MutantDict = {}  # type: ignore


class SQLAlchemyProjectRepository(ProjectRepository):
    @_mutmut_mutated(mutants_xǁSQLAlchemyProjectRepositoryǁ__init____mutmut)
    def __init__(self, db: Session):
        self.db = db
    def xǁSQLAlchemyProjectRepositoryǁ__init____mutmut_orig(self, db: Session):
        self.db = db
    def xǁSQLAlchemyProjectRepositoryǁ__init____mutmut_1(self, db: Session):
        self.db = None

    @_mutmut_mutated(mutants_xǁSQLAlchemyProjectRepositoryǁget_all__mutmut)
    def get_all(self, *, owner_id: int) -> list[Project]:
        return (
            self.db.query(Project)
            .filter(Project.owner_id == owner_id)
            .all()
        )

    def xǁSQLAlchemyProjectRepositoryǁget_all__mutmut_orig(self, *, owner_id: int) -> list[Project]:
        return (
            self.db.query(Project)
            .filter(Project.owner_id == owner_id)
            .all()
        )

    def xǁSQLAlchemyProjectRepositoryǁget_all__mutmut_1(self, *, owner_id: int) -> list[Project]:
        return (
            self.db.query(Project)
            .filter(None)
            .all()
        )

    def xǁSQLAlchemyProjectRepositoryǁget_all__mutmut_2(self, *, owner_id: int) -> list[Project]:
        return (
            self.db.query(None)
            .filter(Project.owner_id == owner_id)
            .all()
        )

    def xǁSQLAlchemyProjectRepositoryǁget_all__mutmut_3(self, *, owner_id: int) -> list[Project]:
        return (
            self.db.query(Project)
            .filter(Project.owner_id != owner_id)
            .all()
        )

    @_mutmut_mutated(mutants_xǁSQLAlchemyProjectRepositoryǁget_by_id__mutmut)
    def get_by_id(self, project_id: int) -> Project | None:
        return self.db.query(Project).filter(Project.id == project_id).first()

    def xǁSQLAlchemyProjectRepositoryǁget_by_id__mutmut_orig(self, project_id: int) -> Project | None:
        return self.db.query(Project).filter(Project.id == project_id).first()

    def xǁSQLAlchemyProjectRepositoryǁget_by_id__mutmut_1(self, project_id: int) -> Project | None:
        return self.db.query(Project).filter(None).first()

    def xǁSQLAlchemyProjectRepositoryǁget_by_id__mutmut_2(self, project_id: int) -> Project | None:
        return self.db.query(None).filter(Project.id == project_id).first()

    def xǁSQLAlchemyProjectRepositoryǁget_by_id__mutmut_3(self, project_id: int) -> Project | None:
        return self.db.query(Project).filter(Project.id != project_id).first()

    @_mutmut_mutated(mutants_xǁSQLAlchemyProjectRepositoryǁget_visible_to_user__mutmut)
    def get_visible_to_user(self, user: User) -> list[Project]:
        query = self.db.query(Project)

        if user.role == UserRole.admin:
            return query.all()

        return (
            query.filter(
                or_(
                    Project.owner_id == user.id,
                    Project.members.any(User.id == user.id),
                )
            )
            .all()
        )

    def xǁSQLAlchemyProjectRepositoryǁget_visible_to_user__mutmut_orig(self, user: User) -> list[Project]:
        query = self.db.query(Project)

        if user.role == UserRole.admin:
            return query.all()

        return (
            query.filter(
                or_(
                    Project.owner_id == user.id,
                    Project.members.any(User.id == user.id),
                )
            )
            .all()
        )

    def xǁSQLAlchemyProjectRepositoryǁget_visible_to_user__mutmut_1(self, user: User) -> list[Project]:
        query = None

        if user.role == UserRole.admin:
            return query.all()

        return (
            query.filter(
                or_(
                    Project.owner_id == user.id,
                    Project.members.any(User.id == user.id),
                )
            )
            .all()
        )

    def xǁSQLAlchemyProjectRepositoryǁget_visible_to_user__mutmut_2(self, user: User) -> list[Project]:
        query = self.db.query(None)

        if user.role == UserRole.admin:
            return query.all()

        return (
            query.filter(
                or_(
                    Project.owner_id == user.id,
                    Project.members.any(User.id == user.id),
                )
            )
            .all()
        )

    def xǁSQLAlchemyProjectRepositoryǁget_visible_to_user__mutmut_3(self, user: User) -> list[Project]:
        query = self.db.query(Project)

        if user.role != UserRole.admin:
            return query.all()

        return (
            query.filter(
                or_(
                    Project.owner_id == user.id,
                    Project.members.any(User.id == user.id),
                )
            )
            .all()
        )

    def xǁSQLAlchemyProjectRepositoryǁget_visible_to_user__mutmut_4(self, user: User) -> list[Project]:
        query = self.db.query(Project)

        if user.role == UserRole.admin:
            return query.all()

        return (
            query.filter(
                None
            )
            .all()
        )

    def xǁSQLAlchemyProjectRepositoryǁget_visible_to_user__mutmut_5(self, user: User) -> list[Project]:
        query = self.db.query(Project)

        if user.role == UserRole.admin:
            return query.all()

        return (
            query.filter(
                or_(
                    None,
                    Project.members.any(User.id == user.id),
                )
            )
            .all()
        )

    def xǁSQLAlchemyProjectRepositoryǁget_visible_to_user__mutmut_6(self, user: User) -> list[Project]:
        query = self.db.query(Project)

        if user.role == UserRole.admin:
            return query.all()

        return (
            query.filter(
                or_(
                    Project.owner_id == user.id,
                    None,
                )
            )
            .all()
        )

    def xǁSQLAlchemyProjectRepositoryǁget_visible_to_user__mutmut_7(self, user: User) -> list[Project]:
        query = self.db.query(Project)

        if user.role == UserRole.admin:
            return query.all()

        return (
            query.filter(
                or_(
                    Project.members.any(User.id == user.id),
                )
            )
            .all()
        )

    def xǁSQLAlchemyProjectRepositoryǁget_visible_to_user__mutmut_8(self, user: User) -> list[Project]:
        query = self.db.query(Project)

        if user.role == UserRole.admin:
            return query.all()

        return (
            query.filter(
                or_(
                    Project.owner_id == user.id,
                    )
            )
            .all()
        )

    def xǁSQLAlchemyProjectRepositoryǁget_visible_to_user__mutmut_9(self, user: User) -> list[Project]:
        query = self.db.query(Project)

        if user.role == UserRole.admin:
            return query.all()

        return (
            query.filter(
                or_(
                    Project.owner_id != user.id,
                    Project.members.any(User.id == user.id),
                )
            )
            .all()
        )

    def xǁSQLAlchemyProjectRepositoryǁget_visible_to_user__mutmut_10(self, user: User) -> list[Project]:
        query = self.db.query(Project)

        if user.role == UserRole.admin:
            return query.all()

        return (
            query.filter(
                or_(
                    Project.owner_id == user.id,
                    Project.members.any(None),
                )
            )
            .all()
        )

    def xǁSQLAlchemyProjectRepositoryǁget_visible_to_user__mutmut_11(self, user: User) -> list[Project]:
        query = self.db.query(Project)

        if user.role == UserRole.admin:
            return query.all()

        return (
            query.filter(
                or_(
                    Project.owner_id == user.id,
                    Project.members.any(User.id != user.id),
                )
            )
            .all()
        )
    
    @_mutmut_mutated(mutants_xǁSQLAlchemyProjectRepositoryǁcreate__mutmut)
    def create(self, payload: ProjectCreate, *, owner_id: int, members=None) -> Project:
        project = Project(
            name=payload.name,
            description=payload.description,
            owner_id=owner_id,
        )
        
        project.members = members or []
        self.db.add(project)
        self.db.commit()
        self.db.refresh(project)
        return project
    
    def xǁSQLAlchemyProjectRepositoryǁcreate__mutmut_orig(self, payload: ProjectCreate, *, owner_id: int, members=None) -> Project:
        project = Project(
            name=payload.name,
            description=payload.description,
            owner_id=owner_id,
        )
        
        project.members = members or []
        self.db.add(project)
        self.db.commit()
        self.db.refresh(project)
        return project
    
    def xǁSQLAlchemyProjectRepositoryǁcreate__mutmut_1(self, payload: ProjectCreate, *, owner_id: int, members=None) -> Project:
        project = None
        
        project.members = members or []
        self.db.add(project)
        self.db.commit()
        self.db.refresh(project)
        return project
    
    def xǁSQLAlchemyProjectRepositoryǁcreate__mutmut_2(self, payload: ProjectCreate, *, owner_id: int, members=None) -> Project:
        project = Project(
            name=None,
            description=payload.description,
            owner_id=owner_id,
        )
        
        project.members = members or []
        self.db.add(project)
        self.db.commit()
        self.db.refresh(project)
        return project
    
    def xǁSQLAlchemyProjectRepositoryǁcreate__mutmut_3(self, payload: ProjectCreate, *, owner_id: int, members=None) -> Project:
        project = Project(
            name=payload.name,
            description=None,
            owner_id=owner_id,
        )
        
        project.members = members or []
        self.db.add(project)
        self.db.commit()
        self.db.refresh(project)
        return project
    
    def xǁSQLAlchemyProjectRepositoryǁcreate__mutmut_4(self, payload: ProjectCreate, *, owner_id: int, members=None) -> Project:
        project = Project(
            name=payload.name,
            description=payload.description,
            owner_id=None,
        )
        
        project.members = members or []
        self.db.add(project)
        self.db.commit()
        self.db.refresh(project)
        return project
    
    def xǁSQLAlchemyProjectRepositoryǁcreate__mutmut_5(self, payload: ProjectCreate, *, owner_id: int, members=None) -> Project:
        project = Project(
            description=payload.description,
            owner_id=owner_id,
        )
        
        project.members = members or []
        self.db.add(project)
        self.db.commit()
        self.db.refresh(project)
        return project
    
    def xǁSQLAlchemyProjectRepositoryǁcreate__mutmut_6(self, payload: ProjectCreate, *, owner_id: int, members=None) -> Project:
        project = Project(
            name=payload.name,
            owner_id=owner_id,
        )
        
        project.members = members or []
        self.db.add(project)
        self.db.commit()
        self.db.refresh(project)
        return project
    
    def xǁSQLAlchemyProjectRepositoryǁcreate__mutmut_7(self, payload: ProjectCreate, *, owner_id: int, members=None) -> Project:
        project = Project(
            name=payload.name,
            description=payload.description,
            )
        
        project.members = members or []
        self.db.add(project)
        self.db.commit()
        self.db.refresh(project)
        return project
    
    def xǁSQLAlchemyProjectRepositoryǁcreate__mutmut_8(self, payload: ProjectCreate, *, owner_id: int, members=None) -> Project:
        project = Project(
            name=payload.name,
            description=payload.description,
            owner_id=owner_id,
        )
        
        project.members = None
        self.db.add(project)
        self.db.commit()
        self.db.refresh(project)
        return project
    
    def xǁSQLAlchemyProjectRepositoryǁcreate__mutmut_9(self, payload: ProjectCreate, *, owner_id: int, members=None) -> Project:
        project = Project(
            name=payload.name,
            description=payload.description,
            owner_id=owner_id,
        )
        
        project.members = members and []
        self.db.add(project)
        self.db.commit()
        self.db.refresh(project)
        return project
    
    def xǁSQLAlchemyProjectRepositoryǁcreate__mutmut_10(self, payload: ProjectCreate, *, owner_id: int, members=None) -> Project:
        project = Project(
            name=payload.name,
            description=payload.description,
            owner_id=owner_id,
        )
        
        project.members = members or []
        self.db.add(None)
        self.db.commit()
        self.db.refresh(project)
        return project
    
    def xǁSQLAlchemyProjectRepositoryǁcreate__mutmut_11(self, payload: ProjectCreate, *, owner_id: int, members=None) -> Project:
        project = Project(
            name=payload.name,
            description=payload.description,
            owner_id=owner_id,
        )
        
        project.members = members or []
        self.db.add(project)
        self.db.commit()
        self.db.refresh(None)
        return project

    @_mutmut_mutated(mutants_xǁSQLAlchemyProjectRepositoryǁupdate__mutmut)
    def update(self, project: Project, payload: ProjectUpdate) -> Project:
        project.name = payload.name
        project.description = payload.description
        self.db.commit()
        self.db.refresh(project)
        return project

    def xǁSQLAlchemyProjectRepositoryǁupdate__mutmut_orig(self, project: Project, payload: ProjectUpdate) -> Project:
        project.name = payload.name
        project.description = payload.description
        self.db.commit()
        self.db.refresh(project)
        return project

    def xǁSQLAlchemyProjectRepositoryǁupdate__mutmut_1(self, project: Project, payload: ProjectUpdate) -> Project:
        project.name = None
        project.description = payload.description
        self.db.commit()
        self.db.refresh(project)
        return project

    def xǁSQLAlchemyProjectRepositoryǁupdate__mutmut_2(self, project: Project, payload: ProjectUpdate) -> Project:
        project.name = payload.name
        project.description = None
        self.db.commit()
        self.db.refresh(project)
        return project

    def xǁSQLAlchemyProjectRepositoryǁupdate__mutmut_3(self, project: Project, payload: ProjectUpdate) -> Project:
        project.name = payload.name
        project.description = payload.description
        self.db.commit()
        self.db.refresh(None)
        return project

    @_mutmut_mutated(mutants_xǁSQLAlchemyProjectRepositoryǁdelete__mutmut)
    def delete(self, project: Project) -> None:
        self.db.delete(project)
        self.db.commit()

    def xǁSQLAlchemyProjectRepositoryǁdelete__mutmut_orig(self, project: Project) -> None:
        self.db.delete(project)
        self.db.commit()

    def xǁSQLAlchemyProjectRepositoryǁdelete__mutmut_1(self, project: Project) -> None:
        self.db.delete(None)
        self.db.commit()

mutants_xǁSQLAlchemyProjectRepositoryǁ__init____mutmut['_mutmut_orig'] = SQLAlchemyProjectRepository.xǁSQLAlchemyProjectRepositoryǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁSQLAlchemyProjectRepositoryǁ__init____mutmut['xǁSQLAlchemyProjectRepositoryǁ__init____mutmut_1'] = SQLAlchemyProjectRepository.xǁSQLAlchemyProjectRepositoryǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁSQLAlchemyProjectRepositoryǁget_all__mutmut['_mutmut_orig'] = SQLAlchemyProjectRepository.xǁSQLAlchemyProjectRepositoryǁget_all__mutmut_orig # type: ignore # mutmut generated
mutants_xǁSQLAlchemyProjectRepositoryǁget_all__mutmut['xǁSQLAlchemyProjectRepositoryǁget_all__mutmut_1'] = SQLAlchemyProjectRepository.xǁSQLAlchemyProjectRepositoryǁget_all__mutmut_1 # type: ignore # mutmut generated
mutants_xǁSQLAlchemyProjectRepositoryǁget_all__mutmut['xǁSQLAlchemyProjectRepositoryǁget_all__mutmut_2'] = SQLAlchemyProjectRepository.xǁSQLAlchemyProjectRepositoryǁget_all__mutmut_2 # type: ignore # mutmut generated
mutants_xǁSQLAlchemyProjectRepositoryǁget_all__mutmut['xǁSQLAlchemyProjectRepositoryǁget_all__mutmut_3'] = SQLAlchemyProjectRepository.xǁSQLAlchemyProjectRepositoryǁget_all__mutmut_3 # type: ignore # mutmut generated

mutants_xǁSQLAlchemyProjectRepositoryǁget_by_id__mutmut['_mutmut_orig'] = SQLAlchemyProjectRepository.xǁSQLAlchemyProjectRepositoryǁget_by_id__mutmut_orig # type: ignore # mutmut generated
mutants_xǁSQLAlchemyProjectRepositoryǁget_by_id__mutmut['xǁSQLAlchemyProjectRepositoryǁget_by_id__mutmut_1'] = SQLAlchemyProjectRepository.xǁSQLAlchemyProjectRepositoryǁget_by_id__mutmut_1 # type: ignore # mutmut generated
mutants_xǁSQLAlchemyProjectRepositoryǁget_by_id__mutmut['xǁSQLAlchemyProjectRepositoryǁget_by_id__mutmut_2'] = SQLAlchemyProjectRepository.xǁSQLAlchemyProjectRepositoryǁget_by_id__mutmut_2 # type: ignore # mutmut generated
mutants_xǁSQLAlchemyProjectRepositoryǁget_by_id__mutmut['xǁSQLAlchemyProjectRepositoryǁget_by_id__mutmut_3'] = SQLAlchemyProjectRepository.xǁSQLAlchemyProjectRepositoryǁget_by_id__mutmut_3 # type: ignore # mutmut generated

mutants_xǁSQLAlchemyProjectRepositoryǁget_visible_to_user__mutmut['_mutmut_orig'] = SQLAlchemyProjectRepository.xǁSQLAlchemyProjectRepositoryǁget_visible_to_user__mutmut_orig # type: ignore # mutmut generated
mutants_xǁSQLAlchemyProjectRepositoryǁget_visible_to_user__mutmut['xǁSQLAlchemyProjectRepositoryǁget_visible_to_user__mutmut_1'] = SQLAlchemyProjectRepository.xǁSQLAlchemyProjectRepositoryǁget_visible_to_user__mutmut_1 # type: ignore # mutmut generated
mutants_xǁSQLAlchemyProjectRepositoryǁget_visible_to_user__mutmut['xǁSQLAlchemyProjectRepositoryǁget_visible_to_user__mutmut_2'] = SQLAlchemyProjectRepository.xǁSQLAlchemyProjectRepositoryǁget_visible_to_user__mutmut_2 # type: ignore # mutmut generated
mutants_xǁSQLAlchemyProjectRepositoryǁget_visible_to_user__mutmut['xǁSQLAlchemyProjectRepositoryǁget_visible_to_user__mutmut_3'] = SQLAlchemyProjectRepository.xǁSQLAlchemyProjectRepositoryǁget_visible_to_user__mutmut_3 # type: ignore # mutmut generated
mutants_xǁSQLAlchemyProjectRepositoryǁget_visible_to_user__mutmut['xǁSQLAlchemyProjectRepositoryǁget_visible_to_user__mutmut_4'] = SQLAlchemyProjectRepository.xǁSQLAlchemyProjectRepositoryǁget_visible_to_user__mutmut_4 # type: ignore # mutmut generated
mutants_xǁSQLAlchemyProjectRepositoryǁget_visible_to_user__mutmut['xǁSQLAlchemyProjectRepositoryǁget_visible_to_user__mutmut_5'] = SQLAlchemyProjectRepository.xǁSQLAlchemyProjectRepositoryǁget_visible_to_user__mutmut_5 # type: ignore # mutmut generated
mutants_xǁSQLAlchemyProjectRepositoryǁget_visible_to_user__mutmut['xǁSQLAlchemyProjectRepositoryǁget_visible_to_user__mutmut_6'] = SQLAlchemyProjectRepository.xǁSQLAlchemyProjectRepositoryǁget_visible_to_user__mutmut_6 # type: ignore # mutmut generated
mutants_xǁSQLAlchemyProjectRepositoryǁget_visible_to_user__mutmut['xǁSQLAlchemyProjectRepositoryǁget_visible_to_user__mutmut_7'] = SQLAlchemyProjectRepository.xǁSQLAlchemyProjectRepositoryǁget_visible_to_user__mutmut_7 # type: ignore # mutmut generated
mutants_xǁSQLAlchemyProjectRepositoryǁget_visible_to_user__mutmut['xǁSQLAlchemyProjectRepositoryǁget_visible_to_user__mutmut_8'] = SQLAlchemyProjectRepository.xǁSQLAlchemyProjectRepositoryǁget_visible_to_user__mutmut_8 # type: ignore # mutmut generated
mutants_xǁSQLAlchemyProjectRepositoryǁget_visible_to_user__mutmut['xǁSQLAlchemyProjectRepositoryǁget_visible_to_user__mutmut_9'] = SQLAlchemyProjectRepository.xǁSQLAlchemyProjectRepositoryǁget_visible_to_user__mutmut_9 # type: ignore # mutmut generated
mutants_xǁSQLAlchemyProjectRepositoryǁget_visible_to_user__mutmut['xǁSQLAlchemyProjectRepositoryǁget_visible_to_user__mutmut_10'] = SQLAlchemyProjectRepository.xǁSQLAlchemyProjectRepositoryǁget_visible_to_user__mutmut_10 # type: ignore # mutmut generated
mutants_xǁSQLAlchemyProjectRepositoryǁget_visible_to_user__mutmut['xǁSQLAlchemyProjectRepositoryǁget_visible_to_user__mutmut_11'] = SQLAlchemyProjectRepository.xǁSQLAlchemyProjectRepositoryǁget_visible_to_user__mutmut_11 # type: ignore # mutmut generated

mutants_xǁSQLAlchemyProjectRepositoryǁcreate__mutmut['_mutmut_orig'] = SQLAlchemyProjectRepository.xǁSQLAlchemyProjectRepositoryǁcreate__mutmut_orig # type: ignore # mutmut generated
mutants_xǁSQLAlchemyProjectRepositoryǁcreate__mutmut['xǁSQLAlchemyProjectRepositoryǁcreate__mutmut_1'] = SQLAlchemyProjectRepository.xǁSQLAlchemyProjectRepositoryǁcreate__mutmut_1 # type: ignore # mutmut generated
mutants_xǁSQLAlchemyProjectRepositoryǁcreate__mutmut['xǁSQLAlchemyProjectRepositoryǁcreate__mutmut_2'] = SQLAlchemyProjectRepository.xǁSQLAlchemyProjectRepositoryǁcreate__mutmut_2 # type: ignore # mutmut generated
mutants_xǁSQLAlchemyProjectRepositoryǁcreate__mutmut['xǁSQLAlchemyProjectRepositoryǁcreate__mutmut_3'] = SQLAlchemyProjectRepository.xǁSQLAlchemyProjectRepositoryǁcreate__mutmut_3 # type: ignore # mutmut generated
mutants_xǁSQLAlchemyProjectRepositoryǁcreate__mutmut['xǁSQLAlchemyProjectRepositoryǁcreate__mutmut_4'] = SQLAlchemyProjectRepository.xǁSQLAlchemyProjectRepositoryǁcreate__mutmut_4 # type: ignore # mutmut generated
mutants_xǁSQLAlchemyProjectRepositoryǁcreate__mutmut['xǁSQLAlchemyProjectRepositoryǁcreate__mutmut_5'] = SQLAlchemyProjectRepository.xǁSQLAlchemyProjectRepositoryǁcreate__mutmut_5 # type: ignore # mutmut generated
mutants_xǁSQLAlchemyProjectRepositoryǁcreate__mutmut['xǁSQLAlchemyProjectRepositoryǁcreate__mutmut_6'] = SQLAlchemyProjectRepository.xǁSQLAlchemyProjectRepositoryǁcreate__mutmut_6 # type: ignore # mutmut generated
mutants_xǁSQLAlchemyProjectRepositoryǁcreate__mutmut['xǁSQLAlchemyProjectRepositoryǁcreate__mutmut_7'] = SQLAlchemyProjectRepository.xǁSQLAlchemyProjectRepositoryǁcreate__mutmut_7 # type: ignore # mutmut generated
mutants_xǁSQLAlchemyProjectRepositoryǁcreate__mutmut['xǁSQLAlchemyProjectRepositoryǁcreate__mutmut_8'] = SQLAlchemyProjectRepository.xǁSQLAlchemyProjectRepositoryǁcreate__mutmut_8 # type: ignore # mutmut generated
mutants_xǁSQLAlchemyProjectRepositoryǁcreate__mutmut['xǁSQLAlchemyProjectRepositoryǁcreate__mutmut_9'] = SQLAlchemyProjectRepository.xǁSQLAlchemyProjectRepositoryǁcreate__mutmut_9 # type: ignore # mutmut generated
mutants_xǁSQLAlchemyProjectRepositoryǁcreate__mutmut['xǁSQLAlchemyProjectRepositoryǁcreate__mutmut_10'] = SQLAlchemyProjectRepository.xǁSQLAlchemyProjectRepositoryǁcreate__mutmut_10 # type: ignore # mutmut generated
mutants_xǁSQLAlchemyProjectRepositoryǁcreate__mutmut['xǁSQLAlchemyProjectRepositoryǁcreate__mutmut_11'] = SQLAlchemyProjectRepository.xǁSQLAlchemyProjectRepositoryǁcreate__mutmut_11 # type: ignore # mutmut generated

mutants_xǁSQLAlchemyProjectRepositoryǁupdate__mutmut['_mutmut_orig'] = SQLAlchemyProjectRepository.xǁSQLAlchemyProjectRepositoryǁupdate__mutmut_orig # type: ignore # mutmut generated
mutants_xǁSQLAlchemyProjectRepositoryǁupdate__mutmut['xǁSQLAlchemyProjectRepositoryǁupdate__mutmut_1'] = SQLAlchemyProjectRepository.xǁSQLAlchemyProjectRepositoryǁupdate__mutmut_1 # type: ignore # mutmut generated
mutants_xǁSQLAlchemyProjectRepositoryǁupdate__mutmut['xǁSQLAlchemyProjectRepositoryǁupdate__mutmut_2'] = SQLAlchemyProjectRepository.xǁSQLAlchemyProjectRepositoryǁupdate__mutmut_2 # type: ignore # mutmut generated
mutants_xǁSQLAlchemyProjectRepositoryǁupdate__mutmut['xǁSQLAlchemyProjectRepositoryǁupdate__mutmut_3'] = SQLAlchemyProjectRepository.xǁSQLAlchemyProjectRepositoryǁupdate__mutmut_3 # type: ignore # mutmut generated

mutants_xǁSQLAlchemyProjectRepositoryǁdelete__mutmut['_mutmut_orig'] = SQLAlchemyProjectRepository.xǁSQLAlchemyProjectRepositoryǁdelete__mutmut_orig # type: ignore # mutmut generated
mutants_xǁSQLAlchemyProjectRepositoryǁdelete__mutmut['xǁSQLAlchemyProjectRepositoryǁdelete__mutmut_1'] = SQLAlchemyProjectRepository.xǁSQLAlchemyProjectRepositoryǁdelete__mutmut_1 # type: ignore # mutmut generated