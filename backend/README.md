# Creating a Backend for our Application
### we will use following tech for our backend
* Neon Postgres Database
* SQLAlchemy ORM
* Alembic for Migration

## 00 Install SQLAlchemy and alembic package
```
pip install sqlalchemy alembic psycopg2
```

## What is SQLAlchemy? and why use it.

## What is Alembic and its usage?


## 01 Create database connection  
```
engine = create_engine(str(os.getenv("POSTGRES_URL")))
Session =  sessionmaker(bind=engine)
```

## 02 Create model classes for the tables
```
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

#add all the other classes you want here
```
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
3. Add ```run_migrations.py``` file in the same location as model and alembic
```
import sys
from dotenv import load_dotenv
from alembic.config import Config
from alembic import command
import os
# Load environment variables from .env
load_dotenv()
postgres_url = os.getenv("POSTGRES_URL")
# Create an Alembic configuration object
alembic_cfg = Config("alembic.ini",config_args={"sqlalchemy.url":postgres_url})

# Check for migration message and optional revision
if len(sys.argv) < 2:
    print("Please provide a migration message.")
    sys.exit(1)

migration_message = sys.argv[1]

revision = sys.argv[2] if len(sys.argv) >= 3 else 'head'

# Run the revision command with a message
command.revision(alembic_cfg, message=migration_message,autogenerate=True)

command.upgrade(alembic_cfg, "head")

```
4. Run the file using
```
python run_migrations.py "add your custom name for the migration"
```