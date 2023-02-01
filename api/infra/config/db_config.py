import sqlite3

class DBConnectionHandler:
  def __init__(self):
    self.__connection_string = "storage.db"
    self.session = None

  def get_connection(self):
    connection = sqlite3.connect(self.__connection_string)
    return connection

  def __enter__(self):
    connection = self.get_connection()
    self.session = connection
    return self

  def __exit__(self, exc_type, exc_val, exc_tb):
    self.session.close()