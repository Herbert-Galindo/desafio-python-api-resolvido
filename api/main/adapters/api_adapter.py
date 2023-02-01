from api.presenters.helpers import HttpRequest

def flask_adapter(request: any, api_route) -> any:

  http_request = None

  if request:
    http_request = HttpRequest(body=request.get_json())
  else:
    http_request = HttpRequest()

  response = api_route.handle(http_request)

  return response