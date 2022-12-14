from pydantic import BaseModel

class Company(BaseModel):

    id_azienda : str
    nome : str
    p_iva : str 
    indirizzo : str
    cap: str
    iban : str
    telefono : str
    email : str
    pec : str
    fax: str