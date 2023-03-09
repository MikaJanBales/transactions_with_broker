import os

from sqlalchemy.ext.declarative import declarative_base


def get_connect_string(env):
    username = env.get("DATABASE_USERNAME", "postgres")
    password = env.get("DATABASE_PASSWORD", "password")
    host = env.get("DATABASE_HOST", "localhost")
    port = env.get("DATABASE_PORT", 5432)
    db_name = env.get("DATABASE_NAME", "transaction")
    if password:
        password = f':{password}'
    connect_string = (
        f"postgresql://{username}{password}@{host}:{port}/{db_name}"
    )
    return connect_string


connect_string = get_connect_string(os.environ)

BaseModel = declarative_base()
