from pydantic import BaseModel, validator
import datetime  
from typing import Optional

class EmployeeCompany(BaseModel):

    id_dipendente : str
    id_azienda : str
    data_inizio_rapporto : datetime.date
    matricola : Optional [str] = ""
    data_fine_rapporto: Optional[datetime.date] = ""
    
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
          
    @validator('matricola')
    def validate_matricola(cls, v):
        if v:
            assert len(v) <= 45, "maximum length for 'matricola' is 45 characters."
            return v                
