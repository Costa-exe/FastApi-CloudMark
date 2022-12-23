from typing import Optional
from pydantic import BaseModel, validator
import datetime  

class Assignment(BaseModel):
    id_commessa: str
    descrizione: Optional[str] = ""
    id_cliente: str
    id_azienda: str
    data_inizio: datetime.date
    data_fine: datetime.date
    
    @validator('id_commessa')
    def assignment_id(cls, v):
        assert len(v) <= 80, 'must be less than 80 characters'
        assert len(v) > 0, 'must be more than 0 characters'
        return v
    
    @validator('descrizione')
    def description(cls, v):
        if v:
            assert len(v) <= 255, 'must be less than 500 characters'
            return v
    
    @validator('id_cliente')
    def customer_id(cls, v):
        assert len(v) <= 120, 'must be less than 120 characters'
        assert len(v) > 0, 'must be more than 0 characters'
        return v
        
    @validator('id_azienda')
    def company_id(cls, v):
        assert len(v) <= 80, 'must be less than 80 characters'
        assert len(v) > 0, 'must be more than 0 characters'
        return v





