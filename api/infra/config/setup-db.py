from db_config import DBConnectionHandler

def create_db():
    with DBConnectionHandler() as db_connection:
        sql_file = open('./api/infra/config/dump.sql', 'r')
        sql_str = sql_file.read()

        db_connection.session.executescript(sql_str)
        db_connection.session.commit()

create_db()