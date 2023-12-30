# Creating a Backend for our Application
### we will use following tech for our backend
* Neon Postgres Database
* SQLAlchemy ORM
* Alembic for Migration

## 00 Install SQLAlchemy and alembic package
```
pip install sqlalchemy alembic
```

## What is SQLAlchemy? and why use it.

## What is Alembic and its usage?


## 01 Create database connection  
```
engine = create_engine(str(os.getenv("POSTGRES_URL")))
Session =  sessionmaker(bind=engine)
```

## 02 Create model classes for the tables

## 03 Now to create and run migrations using alembic

```
alembic init alembic
```
### We need to configure some settings inside alembic to get our auto migrations to work
1. Open ```alembic.ini``` file and comment out line number 63
```
#sqlalchemy.url = driver://user:pass@localhost/dbname
```
2. Open alembic/```env.py``` file and uncomment these lines and add your model classes
```
- # from myapp import mymodel
- # target_metadata = mymodel.Base.metadata
+ from model import Base
+ target_metadata = Base.metadata
- # target_metadata = None
```
