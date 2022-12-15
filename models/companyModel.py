from pydantic import BaseModel, validator

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

    @validator('id_azienda')
    def validate_id(cls, v):
        assert len(v) <= 80, f'maximum length for {v} is 80 characters.'
        assert len(v) > 0, f'{v} must contain at least 1 character.'
        return v

    @validator('nome')
    def validate_id(cls, v):
        assert len(v) <= 90, f'maximum length for {v} is 90 characters.'
        assert len(v) > 0, f'{v} must contain at least 1 character.'
        return v

    @validator('p_iva')
    def validate_id(cls, v):
        assert len(v) <= 11, f'maximum length for {v} is 11 characters.'
        assert len(v) > 0, f'{v} must contain at least 1 character.'
        return v

    @validator('indirizzo')
    def validate_id(cls, v):
        assert len(v) <= 90, f'maximum length for {v} is 90 characters.'
        assert len(v) > 0, f'{v} must contain at least 1 character.'
        return v

    @validator('cap')
    def validate_id(cls, v):
        assert len(v) <= 5, f'maximum length for {v} is 5 characters.'
        assert len(v) > 0, f'{v} must contain at least 1 character.'
        return v

    @validator('iban')
    def validate_id(cls, v):
        assert len(v) <= 27, f'maximum length for {v} is 27 characters.'
        assert len(v) > 0, f'{v} must contain at least 1 character.'
        return v

    @validator('telefono')
    def validate_id(cls, v):
        assert len(v) <= 15, f'maximum length for {v} is 15 characters.'
        assert len(v) > 0, f'{v} must contain at least 1 character.'
        return v

    @validator('email')
    def validate_id(cls, v):
        assert len(v) <= 90, f'maximum length for {v} is 90 characters.'
        assert len(v) > 0, f'{v} must contain at least 1 character.'
        return v

    @validator('pec')
    def validate_id(cls, v):
        assert len(v) <= 45, f'maximum length for {v} is 45 characters.'
        assert len(v) > 0, f'{v} must contain at least 1 character.'
        return v

    @validator('fax')
    def validate_id(cls, v):
        assert len(v) <= 15, f'maximum length for {v} is 15 characters.'
        assert len(v) > 0, f'{v} must contain at least 1 character.'
        return v