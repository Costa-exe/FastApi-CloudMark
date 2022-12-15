from pydantic import BaseModel, validator

class Company_Client(BaseModel):

    id_azienda : str
    id_cliente : str

    @validator('id_azienda')
    def validate_id_azienda(cls, v):
        assert len(v) <= 80, "maximum length for 'id_azienda' is 80 characters."
        assert len(v) > 0, "'id_azienda' must contain at least 1 character."
        return v

    @validator('id_cliente')
    def validate_id_cliente(cls, v):
        assert len(v) <= 80, "maximum length for 'id_cliente' is 80 characters."
        assert len(v) > 0, "'id_cliente' must contain at least 1 character."
        return v