from pydantic import BaseModel,validator
from typing import Optional


class Employee(BaseModel):

    id_dipendente : str
    nome : Optional [str] = ""
    cognome : Optional [str] = "" 
    cf : str
    iban : str
    telefono : Optional [str] = ""
    email : Optional [str] = ""
    id_tipo_contratto : str
    
    @validator('id_dipendente')
    def validate_id_dipendente(cls, v):
        assert len(v) <= 80, "maximum length for 'id_dipendente' is 80 characters."
        assert len(v) > 0, "'id_dipendente' must contain at least 1 character."
        return v 

    @validator('nome')
    def validate_nome(cls, v):
        assert len(v) <= 45, "maximum length for 'nome' is 45 characters."
        return v 

    @validator('cognome')
    def validate_cognome(cls, v):
        assert len(v) <= 45, "maximum length for 'cognome' is 45 characters."
        return v 

    @validator('cf')
    def validate_cf(cls, v):
        assert len(v) <= 16, "maximum length for 'cf' is 16 characters."
        assert len(v) > 0, "'cf' must contain at least 1 character."
        return v             

    @validator('iban')
    def validate_iban(cls, v):
        assert len(v) <= 45, "maximum length for 'iban' is 45 characters."
        assert len(v) > 0, "'iban' must contain at least 1 character."
        return v 

    @validator('id_tipo_contratto')
    def validate_id_tipo_contratto(cls, v):
        assert len(v) <= 80, "maximum length for 'id_tipo_contratto' is 80 characters."
        assert len(v) > 0, "'id_tipo_contratto' must contain at least 1 character."
        return v 

    @validator('email')
    def validate_email(cls, v):
        assert len(v) <= 90, "maximum length for 'email' is 90 characters."
        return v 

    @validator('telefono')
    def validate_telefono(cls, v):
        assert len(v) <= 45, "maximum length for 'telefono' is 45 characters."
        return v                 