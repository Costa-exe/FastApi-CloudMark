import datetime
from pydantic import BaseModel
from typing import Optional
import datetime


class CustomEmployee(BaseModel):

    nome: Optional[str] = ""
    cognome: Optional[str] = ""
    matricola: str
    contratto: str
    assunzione: datetime.date
