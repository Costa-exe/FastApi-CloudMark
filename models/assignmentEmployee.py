from pydantic import BaseModel, validator

class AssignmentEmployee(BaseModel):
    id_commessa: str
    id_dipendente: str
    rate: float

    @validator('id_commessa')
    def assignment_id(cls, v):
        assert len(v) <= 80, 'must be less than 80 characters'
        assert len(v) > 0, 'must be more than 0 characters'
        return v
    
    @validator('id_dipendente')
    def employee_id(cls, v):
        assert len(v) <= 80, 'must be less than 80 characters'
        assert len(v) > 0, 'must be more than 0 characters'
        return v
    
    @validator('rate')
    def rate_v(cls, v):
        assert v > 0, 'must be more than 0'
        return v
