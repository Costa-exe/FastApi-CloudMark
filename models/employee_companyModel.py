from pydantic import BaseModel, validator
import datetime  

class EmployeeCompany(BaseModel):

    id_dipendente : str
    id_azienda : str
    data_inizio_rapporto : datetime.date
    matricola : str
    data_fine_rapporto: datetime.date
    
    @validator('id_dipendente')
    def validate_id_dipendente(cls, v):
        assert len(v) <= 80, "maximum length for 'id_dipendente' is 80 characters."
        assert len(v) > 0, "'id_dipendente' must contain at least 1 character."
        return v    

    @validator('id_azienda')
    def validate_id_azienda(cls, v):
        assert len(v) <= 80, "maximum length for 'id_azienda' is 80 characters."
        assert len(v) > 0, "'id_azienda' must contain at least 1 character."
        return v       

    @validator('data_inizio_rapporto')
    def validate_data_inizio_rapporto(cls, v):
        assert len(v) <= 10, "maximum length for 'data_inizio_rapporto' is 10 characters."
        assert len(v) > 0, "'data_inizio_rapporto' must contain at least 1 character."
        return v                

    @validator('matricola')
    def validate_matricola(cls, v):
        assert len(v) <= 45, "maximum length for 'matricola' is 45 characters."
        assert len(v) > 0, "'matricola' must contain at least 1 character."
        return v                

    @validator('data_fine_rapporto')
    def validate_data_fine_rapporto(cls, v):
        assert len(v) <= 10, "maximum length for 'data_fine_rapporto' is 10 characters."
        assert len(v) > 0, "'data_fine_rapporto' must contain at least 1 character."
        return v     