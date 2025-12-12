import sqlalchemy
from sqlalchemy import create_engine, text
import os

print(sqlalchemy.__version__)

db_connection_string = os.getenv("DB_CONNECTION_STRING")
engine = create_engine(
    db_connection_string,
    connect_args={
       "ssl": {
            "ca": "ssl/cert.pem",
    }
    }
)

def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM jobs"))

    # result.mappings() returns mapping-like rows you can convert to dicts directly
        rows_as_mappings = result.mappings().all()
        jobs_list = [dict(r) for r in rows_as_mappings]
        return jobs_list
    