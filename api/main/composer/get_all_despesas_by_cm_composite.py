from api.infra.repo import DespesasRepository
from api.data.use_cases.get_all_despesas_by_current_month import GetAllDespesasByCurrentMonth
from api.presenters.controllers import GetAllDespesasByCMController

def get_all_despesas_by_cm_composer():
  despesa_repository = DespesasRepository()
  get_all_despesas_use_case = GetAllDespesasByCurrentMonth(
    despesa_repository
  )

  get_all_despesas_controller = GetAllDespesasByCMController(get_all_despesas_use_case)

  return get_all_despesas_controller