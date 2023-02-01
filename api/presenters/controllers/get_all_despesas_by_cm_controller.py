from typing import Type
from api.data.use_cases.get_all_despesas_by_current_month import GetAllDespesasByCurrentMonth as GetAllDespesas
from api.presenters.helpers import HttpRequest, HttpResponse
from api.presenters.errors import HttpErrors

class GetAllDespesasByCMController:
  def __init__(self, getAllDespesas: Type[GetAllDespesas]):
    self.getAllDespesas = getAllDespesas

  def handle(self, httpRequest: Type[HttpRequest]) -> HttpResponse:
    response = self.getAllDespesas.execute()

    return HttpResponse(
      200,
      response["Data"]
    )
