from . despesas_repository import DespesasRepository
from api.infra.config import DBConnectionHandler

despesas_repository = DespesasRepository()

# def test_create_despesa():
#   despesa = despesas_repository.create_despesa(200, "Teste", 1, 1)
#   print(despesa)

def test_get_all_despesas_by_month():
  month = "01"

  despesas = despesas_repository.get_all_despesas_by_month(month)

  print(despesas)

def test_get_despesa():
  id = 9

  despesa = despesas_repository.get_despesa(id)

  print(despesa)
  