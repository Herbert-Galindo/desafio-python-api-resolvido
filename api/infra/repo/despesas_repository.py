from api.infra.config import DBConnectionHandler
from api.domain.models import Despesa
from api.domain.models import TipoPagamento
from api.domain.models import Categoria

class DespesasRepository:
  def create_despesa(
    self,
    valor: float,
    descricao: str,
    tipo_pagamento_id: int,
    categoria_id: int
  ):
    with DBConnectionHandler() as db_connection:

      cursor = db_connection.session.cursor()

      cursor.execute("""
        INSERT INTO despesas (valor, descricao, tipo_pagamento_id, categoria_id)
        VALUES (?,?,?,?)
      """, [valor, descricao, tipo_pagamento_id, categoria_id])

      db_connection.session.commit()

      print("Inseri dados")
      return cursor.lastrowid
    
  def get_all_despesas_by_month(self, month: str):
    with DBConnectionHandler() as db_connection:
      response = db_connection.session.execute("""
        SELECT d.id, d.valor, d.data_compra, d.descricao,
          tp.id, tp.tipo,
          c.id, c.nome, c.descricao
        FROM despesas d
        INNER JOIN tipos_pagamento tp ON tp.id = d.tipo_pagamento_id
        INNER JOIN categorias c ON c.id = d.categoria_id
        WHERE strftime('%m', `data_compra`) = ?
      """, [month]).fetchall()

      if response == None:
        return None

      despesas = map(
        lambda d: Despesa(
          d[0], d[1], d[2], d[3], TipoPagamento(d[4], d[5]), Categoria(d[6], d[7], d[8])
        ) ,response
      )

      return list(despesas)
  
  def get_despesa(self, id: int):
    with DBConnectionHandler() as db_connection:
      response = db_connection.session.execute("""
        SELECT d.id, d.valor, d.data_compra, d.descricao,
          tp.id, tp.tipo,
          c.id, c.nome, c.descricao
        FROM despesas d
        INNER JOIN tipos_pagamento tp ON tp.id = d.tipo_pagamento_id
        INNER JOIN categorias c ON c.id = d.categoria_id
        WHERE d.id = ?;
      """, [id]).fetchone()

      if response == None:
        return None

      despesa = Despesa(
        response[0], response[1], response[2], response[3],
        TipoPagamento(response[4], response[5]), Categoria(response[6], response[7], response[8])
      )

      return despesa