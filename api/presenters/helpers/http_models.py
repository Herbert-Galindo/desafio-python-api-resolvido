class HttpRequest:
  def __init__(self, header = None, body = None, query = None):
    self.header = header
    self.body = body
    self.query = query

  def __repr__(self) -> str:
    return f"HttpRequest (header={self.header}, body={self.body}, query={self.query})"

class HttpResponse:
  def __init__(self, status_code: int, body: any):
    self.status_code = status_code
    self.body = body