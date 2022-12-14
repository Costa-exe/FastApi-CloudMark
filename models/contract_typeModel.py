from pydantic import BaseModel

class ContractType(BaseModel):

    id_tipo_contratto : str
    nome_tipo_contratto : str
    descrizione : str 
    