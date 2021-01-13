from psycopg2 import connect
import app.models as m


def get_connection():
    return connect(database=m.postgres_db,
                   user=m.postgres_user,
                   password=m.postgres_password,
                   host=m.postgres_host)
