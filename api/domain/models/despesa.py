from collections import namedtuple

Despesa = namedtuple(
  "Despesa", "id, valor, data_compra, descricao, tipo_pagamento, categoria"
)