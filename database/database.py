from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
 
# SQLALCHEMY_DATABASE_URL = 'mysql:///./groceries.db'
DB_USER = 'root'
DB_PASSWORD = 'mySQL1avgDB!'
DB_HOST = '34.95.165.137'
DB_PORT = 3306
DB_NAME = 'grocerybud'

# cloud connection name seems not to be needed
# CLOUD_SQL_CONNECTION_NAME = 'fastapi2-382420:southamerica-east1:fastapi0'
# SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}?host=/cloudsql/{CLOUD_SQL_CONNECTION_NAME}"
SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
 
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
 
Base = declarative_base()
 
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()