from abc import ABC, abstractmethod

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


class SQLAlchemyUserRepository(UserRepository):
    def __init__(self, db: Session):
        self.db = db

    def get_all(self) -> list[User]:
        return self.db.query(User).all()

    def get_by_id(self, user_id: int) -> User | None:
        return self.db.query(User).filter(User.id == user_id).first()

    def get_by_email(self, email: str) -> User | None:
        return self.db.query(User).filter(User.email == email).first()

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

    def delete(self, user: User) -> None:
        self.db.delete(user)
        self.db.commit()            