from pydantic import BaseModel, validator
from typing import Optional

class Client(BaseModel):

    id_cliente : str
    nome : Optional[str] = ""
    p_iva : Optional[str] = ""
    indirizzo : Optional[str] = ""
    cap: Optional[str] = ""
    iban : Optional[str] = ""
    telefono : Optional[str] = ""
    email : Optional[str] = ""
    pec : Optional[str] = ""
    fax: Optional[str] = ""

    @validator('id_cliente')
    def validate_id(cls, v):
        assert len(v) <= 80, "maximum length for 'id_cliente' is 80 characters."
        assert len(v) > 0, "'id_cliente' must contain at least 1 character."
        return v

    @validator('nome')
    def validate_nome(cls, v):
        if v:
            assert len(v) <= 90, "maximum length for 'nome' is 90 characters."
            return v

    @validator('p_iva')
    def validate_p_iva(cls, v):
        if v:
            assert len(v) <= 11, "maximum length for 'p_iva' is 11 characters."
            return v

    @validator('indirizzo')
    def validate_indirizzo(cls, v):
        if v:
            assert len(v) <= 90, "maximum length for 'indirizzo' is 90 characters."
            return v

    @validator('cap')
    def validate_cap(cls, v):
        if v:
            assert len(v) <= 5, "maximum length for 'cap' is 5 characters."
            return v

    @validator('iban')
    def validate_iban(cls, v):
        if v:
            assert len(v) <= 27, "maximum length for 'iban' is 27 characters."
            return v

    @validator('telefono')
    def validate_telefono(cls, v):
        if v:
            assert len(v) <= 15, "maximum length for 'telefono' is 15 characters."
            return v

    @validator('email')
    def validate_email(cls, v):
        if v:
            assert len(v) <= 90, "maximum length for 'email' is 90 characters."
            return v

    @validator('pec')
    def validate_pec(cls, v):
        if v:
            assert len(v) <= 90, "maximum length for 'pec' is 90 characters."
            return v

    @validator('fax')
    def validate_fax(cls, v):
        if v:
            assert len(v) <= 15, "maximum length for 'fax' is 15 characters."
            return v