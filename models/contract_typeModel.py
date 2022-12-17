from pydantic import BaseModel, validator

class ContractType(BaseModel):

    id_tipo_contratto : str
    nome_tipo_contratto : str
    descrizione : str 
    
    @validator('id_tipo_contratto')
    def validate_id_tipo_contratto(cls, v):
        assert len(v) <= 80, "maximum length for 'id_tipo_contratto' is 80 characters."
        assert len(v) > 0, "'id_tipo_contratto' must contain at least 1 character."
        return v

    @validator('nome_tipo_contratto')
    def validate_nome_tipo_contratto(cls, v):
        assert len(v) <= 45, "maximum length for 'nome_tipo_contratto' is 45 characters."
        assert len(v) > 0, "'nome_tipo_contratto' must contain at least 1 character."
        return v    

    @validator('descrizione')
    def validate_descrizione(cls, v):
        assert len(v) <= 255, "maximum length for ' descrizione' is 255 characters."
        assert len(v) > 0, "' descrizione' must contain at least 1 character."
        return v        