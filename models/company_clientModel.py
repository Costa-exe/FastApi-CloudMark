from pydantic import BaseModel

class Company_Client(BaseModel):

    id_azienda : str
    id_cliente : str