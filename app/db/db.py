from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import session, sessionmaker
from app.config.cfg import settings

DB_URL = f'postgresql://{settings.DB_USER}:{settings.DB_PASS}@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}'

engine = create_engine(DB_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Dependency


def get_db():
    db = SessionLocal()
    try:
        print('connection to db succeeded')
        db
        yield db
    except Exception as error:
        print('connection to db FAILED')
        print('error', error)
        return error
    finally:
        print('connection to db closed')
        db.close()
