from pydantic import BaseModel

class Employee(BaseModel):

    id_dipendente : str
    nome : str
    cognome : str 
    cf : str
    iban : str
    telefono : str
    email : str
    id_tipo_contratto : str
    