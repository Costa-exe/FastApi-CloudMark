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
        assert len(v) <= 80, "maximum length for 'id_azienda' is 80 characters."
        assert len(v) > 0, "'id_azienda' must contain at least 1 character."
        return v

    @validator('nome')
    def validate_nome(cls, v):
        assert len(v) <= 90, "maximum length for 'nome' is 90 characters."
        assert len(v) > 0,  "'nome' must contain at least 1 character."
        return v

    @validator('p_iva')
    def validate_p_iva(cls, v):
        assert len(v) <= 11, "maximum length for 'p_iva' is 11 characters."
        assert len(v) > 0,  "'p_iva' must contain at least 1 character."
        return v

    @validator('indirizzo')
    def validate_indirizzo(cls, v):
        assert len(v) <= 90, "maximum length for 'indirizzo' is 90 characters."
        assert len(v) > 0, "'indirizzo' must contain at least 1 character."
        return v

    @validator('cap')
    def validate_cap(cls, v):
        assert len(v) <= 5, "maximum length for 'cap' is 5 characters."
        assert len(v) > 0, "'cap' must contain at least 1 character."
        return v

    @validator('iban')
    def validate_iban(cls, v):
        assert len(v) <= 27, "maximum length for 'iban' is 27 characters."
        assert len(v) > 0, "'iban' must contain at least 1 character."
        return v

    @validator('telefono')
    def validate_telefono(cls, v):
        assert len(v) <= 15, "maximum length for 'telefono' is 15 characters."
        assert len(v) > 0, "'telefono' must contain at least 1 character."
        return v

    @validator('email')
    def validate_email(cls, v):
        assert len(v) <= 90, "maximum length for 'email' is 90 characters."
        assert len(v) > 0, "'email' must contain at least 1 character."
        return v

    @validator('pec')
    def validate_pec(cls, v):
        assert len(v) <= 45, "maximum length for 'pec' is 45 characters."
        assert len(v) > 0, "'pec' must contain at least 1 character."
        return v

    @validator('fax')
    def validate_fax(cls, v):
        assert len(v) <= 15, "maximum length for 'fax' is 15 characters."
        assert len(v) > 0, "'fax' must contain at least 1 character."
        return v