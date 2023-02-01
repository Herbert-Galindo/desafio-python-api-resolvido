from . tipo_pagamento_repository import TipoPagamentoRepository

tipo_pagamento_repository = TipoPagamentoRepository()

def test_get_categoria():
  id = 1

  tipo_pagamento = tipo_pagamento_repository.get_tipo_pagamento(id)

  print(tipo_pagamento)