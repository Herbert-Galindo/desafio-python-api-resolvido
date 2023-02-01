from typing import Dict
from typing import List
from datetime import datetime
from api.domain.models import Despesa

class GetAllDespesasByCurrentMonth:
  def __init__(self, despesa_repository):
    self.despesa_repository = despesa_repository

  def execute(self) -> Dict[bool, List[Despesa]]:

    now = datetime.now()
    
    month = ""

    if now.month < 10:
      month = "0" + str(now.month)
    else:
      month = str(now.month)

    despesas = self.despesa_repository.get_all_despesas_by_month(month)

    return {"Success": True, "Data": despesas}
