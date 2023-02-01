from typing import Type
from api.data.use_cases.create_despesa import CreateDespesa
from api.presenters.helpers import HttpRequest, HttpResponse
from api.presenters.errors import HttpErrors

class CreateDespesaController:
  def __init__(self, createDespesaUseCase: Type[CreateDespesa]):
    self.createDespesaUseCase = createDespesaUseCase

  def handle(self, httpRequest: Type[HttpRequest]) -> HttpResponse:
    response = None

    if httpRequest.body:
      body_string_params = httpRequest.body.keys()

      if ("valor" in body_string_params
          and "descricao" in body_string_params
          and "tipo_pagamento_id" in body_string_params
          and "categoria_id" in body_string_params
      ):
        response = self.createDespesaUseCase.execute(
          httpRequest.body["valor"],
          httpRequest.body["descricao"],
          httpRequest.body["tipo_pagamento_id"],
          httpRequest.body["categoria_id"]  
        )
      else:
        response = { "Success": False, "Data": "no field can be empty" }
      
      if response["Success"] is False:
        http_error = HttpErrors.error_400()
        return HttpResponse(
          status_code=http_error["status_code"],
          body=http_error["body"]
        )

      return HttpResponse(
        status_code=201,
        body=response["Data"]
      )
  
    http_error = HttpErrors.error_400()
    return HttpResponse(
          status_code=http_error["status_code"],
          body=http_error["body"]
        )
