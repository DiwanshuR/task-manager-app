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


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_get_db__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_get_db__mutmut)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def x_get_db__mutmut_orig():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def x_get_db__mutmut_1():
    db = None
    try:
        yield db
    finally:
        db.close()

mutants_x_get_db__mutmut['_mutmut_orig'] = x_get_db__mutmut_orig # type: ignore # mutmut generated
mutants_x_get_db__mutmut['x_get_db__mutmut_1'] = x_get_db__mutmut_1 # type: ignore # mutmut generated