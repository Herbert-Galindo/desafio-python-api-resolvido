from flask import Blueprint, jsonify, request
from api.main.composer import create_despesa_composer, get_all_despesas_by_cm_composer
from api.presenters.helpers import HttpRequest

from api.main.adapters import flask_adapter

api_routes_bp = Blueprint("api_routes", __name__)

@api_routes_bp.post("/api/despesas")
def create_despesa():
  message = {}
  response = flask_adapter(request, create_despesa_composer())

  if response.status_code < 300:
    message = {
      "Type": "Despesas",
      "id": response.body.id,
      "valor": response.body.valor,
      "descricao": response.body.descricao,
      "tipo_pagamento": {
        "id": response.body.tipo_pagamento.id,
        "tipo": response.body.tipo_pagamento.tipo
      },
      "categoria": {
        "id": response.body.categoria.id,
        "nome": response.body.categoria.nome,
        "descricao": response.body.categoria.descricao
      },
    }

    return jsonify({"data": message}), response.status_code

  return jsonify({
    "error": {
      "status_code": response.status_code,
      "title": response.body["error"]
    }
  })

@api_routes_bp.get("/api/despesas")
def get_all_despesas_by_current_month():
  message = {}

  response = flask_adapter(None, get_all_despesas_by_cm_composer())

  message = map(
    lambda despesa: {
      "Type": "Despesas",
      "id": despesa.id,
      "valor": despesa.valor,
      "descricao": despesa.descricao,
      "tipo_pagamento": {
        "id": despesa.tipo_pagamento.id,
        "tipo": despesa.tipo_pagamento.tipo
      },
      "categoria": {
        "id": despesa.categoria.id,
        "nome": despesa.categoria.nome,
        "descricao": despesa.categoria.descricao
      },
    }, response.body
  )

  return jsonify({ "data": list(message) }), response.status_code