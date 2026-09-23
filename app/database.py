from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.config import settings

# pool_pre_ping=True tests each connection with a lightweight query
# before handing it to a request. MySQL silently drops idle connections
# after a while -- without this you'd occasionally hit a confusing
# "connection was lost" error on the first request after a quiet spell.
engine = create_engine(settings.DATABASE_URL, pool_pre_ping=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()