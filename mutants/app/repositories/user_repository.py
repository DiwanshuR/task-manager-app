from abc import ABC, abstractmethod

from mutmut.mutation.trampoline import MutantDict
from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated
from sqlalchemy.orm import Session

from app.models.user import User, UserRole


class UserRepository(ABC):
    @abstractmethod
    def get_all(self) -> list[User]:
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, user_id: int) -> User | None:
        raise NotImplementedError

    @abstractmethod
    def get_by_email(self, email: str) -> User | None:
        raise NotImplementedError

    @abstractmethod
    def create(
        self,
        *,
        name: str,
        email: str,
        password_hash: str,
        role: UserRole,
    ) -> User:
        raise NotImplementedError

    @abstractmethod
    def update(
        self,
        user: User,
        *,
        name: str | None = None,
        email: str | None = None,
        role: UserRole | None = None,
    ) -> User:
        raise NotImplementedError

    @abstractmethod
    def delete(self, user: User) -> None:
        raise NotImplementedError


mutants_xǁSQLAlchemyUserRepositoryǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁSQLAlchemyUserRepositoryǁget_all__mutmut: MutantDict = {}  # type: ignore
mutants_xǁSQLAlchemyUserRepositoryǁget_by_id__mutmut: MutantDict = {}  # type: ignore
mutants_xǁSQLAlchemyUserRepositoryǁget_by_email__mutmut: MutantDict = {}  # type: ignore
mutants_xǁSQLAlchemyUserRepositoryǁcreate__mutmut: MutantDict = {}  # type: ignore
mutants_xǁSQLAlchemyUserRepositoryǁupdate__mutmut: MutantDict = {}  # type: ignore
mutants_xǁSQLAlchemyUserRepositoryǁdelete__mutmut: MutantDict = {}  # type: ignore


class SQLAlchemyUserRepository(UserRepository):
    @_mutmut_mutated(mutants_xǁSQLAlchemyUserRepositoryǁ__init____mutmut)
    def __init__(self, db: Session):
        self.db = db

    def xǁSQLAlchemyUserRepositoryǁ__init____mutmut_orig(self, db: Session):
        self.db = db

    def xǁSQLAlchemyUserRepositoryǁ__init____mutmut_1(self, db: Session):
        self.db = None

    @_mutmut_mutated(mutants_xǁSQLAlchemyUserRepositoryǁget_all__mutmut)
    def get_all(self) -> list[User]:
        return self.db.query(User).all()

    def xǁSQLAlchemyUserRepositoryǁget_all__mutmut_orig(self) -> list[User]:
        return self.db.query(User).all()

    def xǁSQLAlchemyUserRepositoryǁget_all__mutmut_1(self) -> list[User]:
        return self.db.query(None).all()

    @_mutmut_mutated(mutants_xǁSQLAlchemyUserRepositoryǁget_by_id__mutmut)
    def get_by_id(self, user_id: int) -> User | None:
        return self.db.query(User).filter(User.id == user_id).first()

    def xǁSQLAlchemyUserRepositoryǁget_by_id__mutmut_orig(self, user_id: int) -> User | None:
        return self.db.query(User).filter(User.id == user_id).first()

    def xǁSQLAlchemyUserRepositoryǁget_by_id__mutmut_1(self, user_id: int) -> User | None:
        return self.db.query(User).filter(None).first()

    def xǁSQLAlchemyUserRepositoryǁget_by_id__mutmut_2(self, user_id: int) -> User | None:
        return self.db.query(None).filter(User.id == user_id).first()

    def xǁSQLAlchemyUserRepositoryǁget_by_id__mutmut_3(self, user_id: int) -> User | None:
        return self.db.query(User).filter(User.id != user_id).first()

    @_mutmut_mutated(mutants_xǁSQLAlchemyUserRepositoryǁget_by_email__mutmut)
    def get_by_email(self, email: str) -> User | None:
        return self.db.query(User).filter(User.email == email).first()

    def xǁSQLAlchemyUserRepositoryǁget_by_email__mutmut_orig(self, email: str) -> User | None:
        return self.db.query(User).filter(User.email == email).first()

    def xǁSQLAlchemyUserRepositoryǁget_by_email__mutmut_1(self, email: str) -> User | None:
        return self.db.query(User).filter(None).first()

    def xǁSQLAlchemyUserRepositoryǁget_by_email__mutmut_2(self, email: str) -> User | None:
        return self.db.query(None).filter(User.email == email).first()

    def xǁSQLAlchemyUserRepositoryǁget_by_email__mutmut_3(self, email: str) -> User | None:
        return self.db.query(User).filter(User.email != email).first()

    @_mutmut_mutated(mutants_xǁSQLAlchemyUserRepositoryǁcreate__mutmut)
    def create(
        self,
        *,
        name: str,
        email: str,
        password_hash: str,
        role: UserRole,
    ) -> User:
        user = User(
            name=name,
            email=email,
            password_hash=password_hash,
            role=role,
        )
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def xǁSQLAlchemyUserRepositoryǁcreate__mutmut_orig(
        self,
        *,
        name: str,
        email: str,
        password_hash: str,
        role: UserRole,
    ) -> User:
        user = User(
            name=name,
            email=email,
            password_hash=password_hash,
            role=role,
        )
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def xǁSQLAlchemyUserRepositoryǁcreate__mutmut_1(
        self,
        *,
        name: str,
        email: str,
        password_hash: str,
        role: UserRole,
    ) -> User:
        user = None
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def xǁSQLAlchemyUserRepositoryǁcreate__mutmut_2(
        self,
        *,
        name: str,
        email: str,
        password_hash: str,
        role: UserRole,
    ) -> User:
        user = User(
            name=None,
            email=email,
            password_hash=password_hash,
            role=role,
        )
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def xǁSQLAlchemyUserRepositoryǁcreate__mutmut_3(
        self,
        *,
        name: str,
        email: str,
        password_hash: str,
        role: UserRole,
    ) -> User:
        user = User(
            name=name,
            email=None,
            password_hash=password_hash,
            role=role,
        )
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def xǁSQLAlchemyUserRepositoryǁcreate__mutmut_4(
        self,
        *,
        name: str,
        email: str,
        password_hash: str,
        role: UserRole,
    ) -> User:
        user = User(
            name=name,
            email=email,
            password_hash=None,
            role=role,
        )
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def xǁSQLAlchemyUserRepositoryǁcreate__mutmut_5(
        self,
        *,
        name: str,
        email: str,
        password_hash: str,
        role: UserRole,
    ) -> User:
        user = User(
            name=name,
            email=email,
            password_hash=password_hash,
            role=None,
        )
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def xǁSQLAlchemyUserRepositoryǁcreate__mutmut_6(
        self,
        *,
        name: str,
        email: str,
        password_hash: str,
        role: UserRole,
    ) -> User:
        user = User(
            email=email,
            password_hash=password_hash,
            role=role,
        )
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def xǁSQLAlchemyUserRepositoryǁcreate__mutmut_7(
        self,
        *,
        name: str,
        email: str,
        password_hash: str,
        role: UserRole,
    ) -> User:
        user = User(
            name=name,
            password_hash=password_hash,
            role=role,
        )
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def xǁSQLAlchemyUserRepositoryǁcreate__mutmut_8(
        self,
        *,
        name: str,
        email: str,
        password_hash: str,
        role: UserRole,
    ) -> User:
        user = User(
            name=name,
            email=email,
            role=role,
        )
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def xǁSQLAlchemyUserRepositoryǁcreate__mutmut_9(
        self,
        *,
        name: str,
        email: str,
        password_hash: str,
        role: UserRole,
    ) -> User:
        user = User(
            name=name,
            email=email,
            password_hash=password_hash,
        )
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def xǁSQLAlchemyUserRepositoryǁcreate__mutmut_10(
        self,
        *,
        name: str,
        email: str,
        password_hash: str,
        role: UserRole,
    ) -> User:
        user = User(
            name=name,
            email=email,
            password_hash=password_hash,
            role=role,
        )
        self.db.add(None)
        self.db.commit()
        self.db.refresh(user)
        return user

    def xǁSQLAlchemyUserRepositoryǁcreate__mutmut_11(
        self,
        *,
        name: str,
        email: str,
        password_hash: str,
        role: UserRole,
    ) -> User:
        user = User(
            name=name,
            email=email,
            password_hash=password_hash,
            role=role,
        )
        self.db.add(user)
        self.db.commit()
        self.db.refresh(None)
        return user

    @_mutmut_mutated(mutants_xǁSQLAlchemyUserRepositoryǁupdate__mutmut)
    def update(
        self,
        user: User,
        *,
        name: str | None = None,
        email: str | None = None,
        role: UserRole | None = None,
    ) -> User:
        if name is not None:
            user.name = name
        if email is not None:
            user.email = email
        if role is not None:
            user.role = role

        self.db.commit()
        self.db.refresh(user)
        return user

    def xǁSQLAlchemyUserRepositoryǁupdate__mutmut_orig(
        self,
        user: User,
        *,
        name: str | None = None,
        email: str | None = None,
        role: UserRole | None = None,
    ) -> User:
        if name is not None:
            user.name = name
        if email is not None:
            user.email = email
        if role is not None:
            user.role = role

        self.db.commit()
        self.db.refresh(user)
        return user

    def xǁSQLAlchemyUserRepositoryǁupdate__mutmut_1(
        self,
        user: User,
        *,
        name: str | None = None,
        email: str | None = None,
        role: UserRole | None = None,
    ) -> User:
        if name is None:
            user.name = name
        if email is not None:
            user.email = email
        if role is not None:
            user.role = role

        self.db.commit()
        self.db.refresh(user)
        return user

    def xǁSQLAlchemyUserRepositoryǁupdate__mutmut_2(
        self,
        user: User,
        *,
        name: str | None = None,
        email: str | None = None,
        role: UserRole | None = None,
    ) -> User:
        if name is not None:
            user.name = None
        if email is not None:
            user.email = email
        if role is not None:
            user.role = role

        self.db.commit()
        self.db.refresh(user)
        return user

    def xǁSQLAlchemyUserRepositoryǁupdate__mutmut_3(
        self,
        user: User,
        *,
        name: str | None = None,
        email: str | None = None,
        role: UserRole | None = None,
    ) -> User:
        if name is not None:
            user.name = name
        if email is None:
            user.email = email
        if role is not None:
            user.role = role

        self.db.commit()
        self.db.refresh(user)
        return user

    def xǁSQLAlchemyUserRepositoryǁupdate__mutmut_4(
        self,
        user: User,
        *,
        name: str | None = None,
        email: str | None = None,
        role: UserRole | None = None,
    ) -> User:
        if name is not None:
            user.name = name
        if email is not None:
            user.email = None
        if role is not None:
            user.role = role

        self.db.commit()
        self.db.refresh(user)
        return user

    def xǁSQLAlchemyUserRepositoryǁupdate__mutmut_5(
        self,
        user: User,
        *,
        name: str | None = None,
        email: str | None = None,
        role: UserRole | None = None,
    ) -> User:
        if name is not None:
            user.name = name
        if email is not None:
            user.email = email
        if role is None:
            user.role = role

        self.db.commit()
        self.db.refresh(user)
        return user

    def xǁSQLAlchemyUserRepositoryǁupdate__mutmut_6(
        self,
        user: User,
        *,
        name: str | None = None,
        email: str | None = None,
        role: UserRole | None = None,
    ) -> User:
        if name is not None:
            user.name = name
        if email is not None:
            user.email = email
        if role is not None:
            user.role = None

        self.db.commit()
        self.db.refresh(user)
        return user

    def xǁSQLAlchemyUserRepositoryǁupdate__mutmut_7(
        self,
        user: User,
        *,
        name: str | None = None,
        email: str | None = None,
        role: UserRole | None = None,
    ) -> User:
        if name is not None:
            user.name = name
        if email is not None:
            user.email = email
        if role is not None:
            user.role = role

        self.db.commit()
        self.db.refresh(None)
        return user

    @_mutmut_mutated(mutants_xǁSQLAlchemyUserRepositoryǁdelete__mutmut)
    def delete(self, user: User) -> None:
        self.db.delete(user)
        self.db.commit()

    def xǁSQLAlchemyUserRepositoryǁdelete__mutmut_orig(self, user: User) -> None:
        self.db.delete(user)
        self.db.commit()

    def xǁSQLAlchemyUserRepositoryǁdelete__mutmut_1(self, user: User) -> None:
        self.db.delete(None)
        self.db.commit()


mutants_xǁSQLAlchemyUserRepositoryǁ__init____mutmut["_mutmut_orig"] = (
    SQLAlchemyUserRepository.xǁSQLAlchemyUserRepositoryǁ__init____mutmut_orig
)  # type: ignore # mutmut generated
mutants_xǁSQLAlchemyUserRepositoryǁ__init____mutmut[
    "xǁSQLAlchemyUserRepositoryǁ__init____mutmut_1"
] = SQLAlchemyUserRepository.xǁSQLAlchemyUserRepositoryǁ__init____mutmut_1  # type: ignore # mutmut generated

mutants_xǁSQLAlchemyUserRepositoryǁget_all__mutmut["_mutmut_orig"] = (
    SQLAlchemyUserRepository.xǁSQLAlchemyUserRepositoryǁget_all__mutmut_orig
)  # type: ignore # mutmut generated
mutants_xǁSQLAlchemyUserRepositoryǁget_all__mutmut[
    "xǁSQLAlchemyUserRepositoryǁget_all__mutmut_1"
] = SQLAlchemyUserRepository.xǁSQLAlchemyUserRepositoryǁget_all__mutmut_1  # type: ignore # mutmut generated

mutants_xǁSQLAlchemyUserRepositoryǁget_by_id__mutmut["_mutmut_orig"] = (
    SQLAlchemyUserRepository.xǁSQLAlchemyUserRepositoryǁget_by_id__mutmut_orig
)  # type: ignore # mutmut generated
mutants_xǁSQLAlchemyUserRepositoryǁget_by_id__mutmut[
    "xǁSQLAlchemyUserRepositoryǁget_by_id__mutmut_1"
] = SQLAlchemyUserRepository.xǁSQLAlchemyUserRepositoryǁget_by_id__mutmut_1  # type: ignore # mutmut generated
mutants_xǁSQLAlchemyUserRepositoryǁget_by_id__mutmut[
    "xǁSQLAlchemyUserRepositoryǁget_by_id__mutmut_2"
] = SQLAlchemyUserRepository.xǁSQLAlchemyUserRepositoryǁget_by_id__mutmut_2  # type: ignore # mutmut generated
mutants_xǁSQLAlchemyUserRepositoryǁget_by_id__mutmut[
    "xǁSQLAlchemyUserRepositoryǁget_by_id__mutmut_3"
] = SQLAlchemyUserRepository.xǁSQLAlchemyUserRepositoryǁget_by_id__mutmut_3  # type: ignore # mutmut generated

mutants_xǁSQLAlchemyUserRepositoryǁget_by_email__mutmut["_mutmut_orig"] = (
    SQLAlchemyUserRepository.xǁSQLAlchemyUserRepositoryǁget_by_email__mutmut_orig
)  # type: ignore # mutmut generated
mutants_xǁSQLAlchemyUserRepositoryǁget_by_email__mutmut[
    "xǁSQLAlchemyUserRepositoryǁget_by_email__mutmut_1"
] = SQLAlchemyUserRepository.xǁSQLAlchemyUserRepositoryǁget_by_email__mutmut_1  # type: ignore # mutmut generated
mutants_xǁSQLAlchemyUserRepositoryǁget_by_email__mutmut[
    "xǁSQLAlchemyUserRepositoryǁget_by_email__mutmut_2"
] = SQLAlchemyUserRepository.xǁSQLAlchemyUserRepositoryǁget_by_email__mutmut_2  # type: ignore # mutmut generated
mutants_xǁSQLAlchemyUserRepositoryǁget_by_email__mutmut[
    "xǁSQLAlchemyUserRepositoryǁget_by_email__mutmut_3"
] = SQLAlchemyUserRepository.xǁSQLAlchemyUserRepositoryǁget_by_email__mutmut_3  # type: ignore # mutmut generated

mutants_xǁSQLAlchemyUserRepositoryǁcreate__mutmut["_mutmut_orig"] = (
    SQLAlchemyUserRepository.xǁSQLAlchemyUserRepositoryǁcreate__mutmut_orig
)  # type: ignore # mutmut generated
mutants_xǁSQLAlchemyUserRepositoryǁcreate__mutmut["xǁSQLAlchemyUserRepositoryǁcreate__mutmut_1"] = (
    SQLAlchemyUserRepository.xǁSQLAlchemyUserRepositoryǁcreate__mutmut_1
)  # type: ignore # mutmut generated
mutants_xǁSQLAlchemyUserRepositoryǁcreate__mutmut["xǁSQLAlchemyUserRepositoryǁcreate__mutmut_2"] = (
    SQLAlchemyUserRepository.xǁSQLAlchemyUserRepositoryǁcreate__mutmut_2
)  # type: ignore # mutmut generated
mutants_xǁSQLAlchemyUserRepositoryǁcreate__mutmut["xǁSQLAlchemyUserRepositoryǁcreate__mutmut_3"] = (
    SQLAlchemyUserRepository.xǁSQLAlchemyUserRepositoryǁcreate__mutmut_3
)  # type: ignore # mutmut generated
mutants_xǁSQLAlchemyUserRepositoryǁcreate__mutmut["xǁSQLAlchemyUserRepositoryǁcreate__mutmut_4"] = (
    SQLAlchemyUserRepository.xǁSQLAlchemyUserRepositoryǁcreate__mutmut_4
)  # type: ignore # mutmut generated
mutants_xǁSQLAlchemyUserRepositoryǁcreate__mutmut["xǁSQLAlchemyUserRepositoryǁcreate__mutmut_5"] = (
    SQLAlchemyUserRepository.xǁSQLAlchemyUserRepositoryǁcreate__mutmut_5
)  # type: ignore # mutmut generated
mutants_xǁSQLAlchemyUserRepositoryǁcreate__mutmut["xǁSQLAlchemyUserRepositoryǁcreate__mutmut_6"] = (
    SQLAlchemyUserRepository.xǁSQLAlchemyUserRepositoryǁcreate__mutmut_6
)  # type: ignore # mutmut generated
mutants_xǁSQLAlchemyUserRepositoryǁcreate__mutmut["xǁSQLAlchemyUserRepositoryǁcreate__mutmut_7"] = (
    SQLAlchemyUserRepository.xǁSQLAlchemyUserRepositoryǁcreate__mutmut_7
)  # type: ignore # mutmut generated
mutants_xǁSQLAlchemyUserRepositoryǁcreate__mutmut["xǁSQLAlchemyUserRepositoryǁcreate__mutmut_8"] = (
    SQLAlchemyUserRepository.xǁSQLAlchemyUserRepositoryǁcreate__mutmut_8
)  # type: ignore # mutmut generated
mutants_xǁSQLAlchemyUserRepositoryǁcreate__mutmut["xǁSQLAlchemyUserRepositoryǁcreate__mutmut_9"] = (
    SQLAlchemyUserRepository.xǁSQLAlchemyUserRepositoryǁcreate__mutmut_9
)  # type: ignore # mutmut generated
mutants_xǁSQLAlchemyUserRepositoryǁcreate__mutmut[
    "xǁSQLAlchemyUserRepositoryǁcreate__mutmut_10"
] = SQLAlchemyUserRepository.xǁSQLAlchemyUserRepositoryǁcreate__mutmut_10  # type: ignore # mutmut generated
mutants_xǁSQLAlchemyUserRepositoryǁcreate__mutmut[
    "xǁSQLAlchemyUserRepositoryǁcreate__mutmut_11"
] = SQLAlchemyUserRepository.xǁSQLAlchemyUserRepositoryǁcreate__mutmut_11  # type: ignore # mutmut generated

mutants_xǁSQLAlchemyUserRepositoryǁupdate__mutmut["_mutmut_orig"] = (
    SQLAlchemyUserRepository.xǁSQLAlchemyUserRepositoryǁupdate__mutmut_orig
)  # type: ignore # mutmut generated
mutants_xǁSQLAlchemyUserRepositoryǁupdate__mutmut["xǁSQLAlchemyUserRepositoryǁupdate__mutmut_1"] = (
    SQLAlchemyUserRepository.xǁSQLAlchemyUserRepositoryǁupdate__mutmut_1
)  # type: ignore # mutmut generated
mutants_xǁSQLAlchemyUserRepositoryǁupdate__mutmut["xǁSQLAlchemyUserRepositoryǁupdate__mutmut_2"] = (
    SQLAlchemyUserRepository.xǁSQLAlchemyUserRepositoryǁupdate__mutmut_2
)  # type: ignore # mutmut generated
mutants_xǁSQLAlchemyUserRepositoryǁupdate__mutmut["xǁSQLAlchemyUserRepositoryǁupdate__mutmut_3"] = (
    SQLAlchemyUserRepository.xǁSQLAlchemyUserRepositoryǁupdate__mutmut_3
)  # type: ignore # mutmut generated
mutants_xǁSQLAlchemyUserRepositoryǁupdate__mutmut["xǁSQLAlchemyUserRepositoryǁupdate__mutmut_4"] = (
    SQLAlchemyUserRepository.xǁSQLAlchemyUserRepositoryǁupdate__mutmut_4
)  # type: ignore # mutmut generated
mutants_xǁSQLAlchemyUserRepositoryǁupdate__mutmut["xǁSQLAlchemyUserRepositoryǁupdate__mutmut_5"] = (
    SQLAlchemyUserRepository.xǁSQLAlchemyUserRepositoryǁupdate__mutmut_5
)  # type: ignore # mutmut generated
mutants_xǁSQLAlchemyUserRepositoryǁupdate__mutmut["xǁSQLAlchemyUserRepositoryǁupdate__mutmut_6"] = (
    SQLAlchemyUserRepository.xǁSQLAlchemyUserRepositoryǁupdate__mutmut_6
)  # type: ignore # mutmut generated
mutants_xǁSQLAlchemyUserRepositoryǁupdate__mutmut["xǁSQLAlchemyUserRepositoryǁupdate__mutmut_7"] = (
    SQLAlchemyUserRepository.xǁSQLAlchemyUserRepositoryǁupdate__mutmut_7
)  # type: ignore # mutmut generated

mutants_xǁSQLAlchemyUserRepositoryǁdelete__mutmut["_mutmut_orig"] = (
    SQLAlchemyUserRepository.xǁSQLAlchemyUserRepositoryǁdelete__mutmut_orig
)  # type: ignore # mutmut generated
mutants_xǁSQLAlchemyUserRepositoryǁdelete__mutmut["xǁSQLAlchemyUserRepositoryǁdelete__mutmut_1"] = (
    SQLAlchemyUserRepository.xǁSQLAlchemyUserRepositoryǁdelete__mutmut_1
)  # type: ignore # mutmut generated
