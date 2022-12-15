from pydantic import BaseModel, validator

class Company_Client(BaseModel):

    id_azienda : str
    id_cliente : str

    @validator('id_azienda')
    def validate_id(cls, v):
        assert len(v) <= 80, f'maximum length for {v} is 80 characters.'
        assert len(v) > 0, f'{v} must contain at least 1 character.'
        return v

    @validator('id_cliente')
    def validate_id(cls, v):
        assert len(v) <= 80, f'maximum length for {v} is 80 characters.'
        assert len(v) > 0, f'{v} must contain at least 1 character.'
        return v