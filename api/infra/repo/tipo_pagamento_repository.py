from api.infra.config import DBConnectionHandler
from api.domain.models import TipoPagamento

class TipoPagamentoRepository:
  def get_tipo_pagamento(self, id: int):
    with DBConnectionHandler() as db_connection:
      response = db_connection.session.execute("""
        SELECT * FROM tipos_pagamento WHERE id = ? 
      """, [id]).fetchone()

      if response == None:
        return None

      return TipoPagamento(
        id=response[0],
        tipo=response[1]
      )