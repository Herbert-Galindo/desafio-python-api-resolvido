from typing import Dict
from api.domain.models import Despesa

class CreateDespesa:
  def __init__(self, despesa_repository, categoria_repository, tipo_pagamento_repository):
    self.despesa_repository = despesa_repository
    self.categoria_repository = categoria_repository
    self.tipo_pagamento_repository = tipo_pagamento_repository

  def execute(
    self,
    valor: float,
    descricao: str,
    tipo_pagamento_id: int,
    categoria_id: int
  ) -> Dict[bool, Despesa]:

    validate_entry = isinstance(valor, int) and isinstance(descricao, str) and isinstance(tipo_pagamento_id, int) and isinstance(categoria_id, int)

    if not validate_entry:
      return {"Success": False, "Data": None}

    tipo_pagamento = self.tipo_pagamento_repository.get_tipo_pagamento(tipo_pagamento_id)
    categoria = self.categoria_repository.get_categoria(categoria_id)

    if tipo_pagamento is None or categoria is None:
      return {"Success": False, "Data": None}

    id = self.despesa_repository.create_despesa(
      valor, descricao, tipo_pagamento_id, categoria_id
    )

    despesa = self.despesa_repository.get_despesa(id)

    return {"Success": True, "Data": despesa}
