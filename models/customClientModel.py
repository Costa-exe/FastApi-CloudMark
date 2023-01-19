from pydantic import BaseModel
from typing import Optional


class CustomClient(BaseModel):

    nome: Optional[str] = ""
    p_iva: Optional[str] = ""
    email: Optional[str] = ""
    telefono: Optional[str] = ""
    indirizzo: Optional[str] = ""
    cap: Optional[str] = ""
    commesse_attive: int
