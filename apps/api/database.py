from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# url format: postgresql://<username>:<password>@<host>:<port>/<database_name>
SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:Bright#1270@db:5432/blog_post_manager'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()