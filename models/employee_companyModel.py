from pydantic import BaseModel

class EmployeeCompany(BaseModel):

    id_dipendente : str
    id_azienda : str
    data_inizio_rapporto : str 
    matricola : str
    data_fine_rapporto: str
    