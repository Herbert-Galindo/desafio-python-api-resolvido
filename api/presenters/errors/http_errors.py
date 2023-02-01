class HttpErrors:
  @staticmethod
  def error_400():
    return {
      "status_code": 400,
      "body": {
        "error": "BAD REQUEST"
      }
    }
