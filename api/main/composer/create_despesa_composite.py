from api.infra.repo import DespesasRepository, CategoriaRepository, TipoPagamentoRepository
from api.data.use_cases.create_despesa import CreateDespesa
from api.presenters.controllers import CreateDespesaController

def create_despesa_composer():
  despesa_repository = DespesasRepository()
  categoria_repository = CategoriaRepository()
  tipo_pagamento_repository = TipoPagamentoRepository()
  create_despesa_use_case = CreateDespesa(
    despesa_repository, categoria_repository, tipo_pagamento_repository
  )

  create_despesa_controller = CreateDespesaController(create_despesa_use_case)

  return create_despesa_controller