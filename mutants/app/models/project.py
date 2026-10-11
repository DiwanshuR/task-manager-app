from sqlalchemy import Column, Integer, String, DateTime, Table, ForeignKey
from sqlalchemy.orm import relationship, validates
from sqlalchemy.sql import func
from app.database import Base


project_members = Table(
    "project_members",
    Base.metadata,
    Column(
        "project_id",
        Integer,
        ForeignKey("projects.id", ondelete="CASCADE"),
        primary_key=True,
    ),
    Column(
        "user_id",
        Integer,
        ForeignKey("users.id", ondelete="CASCADE"),
        primary_key=True,
    ),
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁProjectǁ__eq____mutmut: MutantDict = {}  # type: ignore


class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    description = Column(String(1000), nullable=True)
    owner_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    owner = relationship("User", back_populates="projects")
    tasks = relationship("Task", back_populates="project", cascade="all, delete-orphan")
    members = relationship(
        "User",
        secondary=project_members,
        back_populates="assigned_projects",
    )
    
    @validates("name")
    def validate_name(self, key: str, value: str) -> str:
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Project name cannot be empty")
        return value.strip()

    @classmethod
    def from_dict(cls, data: dict) -> "Project":
        return cls(**data)

    def __repr__(self) -> str:
        return (
            f"Project(id={self.id!r}, name={self.name!r}, "
            f"owner_id={self.owner_id!r})"
        )

    @_mutmut_mutated(mutants_xǁProjectǁ__eq____mutmut)
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Project):
            return NotImplemented

        return (
            self.id,
            self.name,
            self.description,
            self.owner_id,
        ) == (
            other.id,
            other.name,
            other.description,
            other.owner_id,
        )

    def xǁProjectǁ__eq____mutmut_orig(self, other: object) -> bool:
        if not isinstance(other, Project):
            return NotImplemented

        return (
            self.id,
            self.name,
            self.description,
            self.owner_id,
        ) == (
            other.id,
            other.name,
            other.description,
            other.owner_id,
        )

    def xǁProjectǁ__eq____mutmut_1(self, other: object) -> bool:
        if isinstance(other, Project):
            return NotImplemented

        return (
            self.id,
            self.name,
            self.description,
            self.owner_id,
        ) == (
            other.id,
            other.name,
            other.description,
            other.owner_id,
        )

    def xǁProjectǁ__eq____mutmut_2(self, other: object) -> bool:
        if not isinstance(other, Project):
            return NotImplemented

        return (
            self.id,
            self.name,
            self.description,
            self.owner_id,
        ) != (
            other.id,
            other.name,
            other.description,
            other.owner_id,
        )

mutants_xǁProjectǁ__eq____mutmut['_mutmut_orig'] = Project.xǁProjectǁ__eq____mutmut_orig # type: ignore # mutmut generated
mutants_xǁProjectǁ__eq____mutmut['xǁProjectǁ__eq____mutmut_1'] = Project.xǁProjectǁ__eq____mutmut_1 # type: ignore # mutmut generated
mutants_xǁProjectǁ__eq____mutmut['xǁProjectǁ__eq____mutmut_2'] = Project.xǁProjectǁ__eq____mutmut_2 # type: ignore # mutmut generated