from api.infra.config import DBConnectionHandler
from api.domain.models import Categoria

class CategoriaRepository:
  def get_categoria(self, id: int):
    with DBConnectionHandler() as db_connection:
      response = db_connection.session.execute("""
        SELECT * FROM categorias WHERE id = ?
      """, [id]).fetchone()

      if response == None:
        return None

      return Categoria(
        id=response[0],
        nome=response[1],
        descricao=response[2]
      )