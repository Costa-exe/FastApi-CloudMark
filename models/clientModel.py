from pydantic import BaseModel

class Client(BaseModel):

    id_cliente : str
    nome : str
    p_iva : str 
    indirizzo : str
    cap: str
    iban : str
    telefono : str
    email : str
    pec : str
    fax: str