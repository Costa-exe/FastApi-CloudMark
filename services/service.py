from dto.employeeDto import EmployeeDto
from dto.employee_companyDto import EmployeeCompanyDto
from dto.contract_typeDto import ContractTypeDto

from models.employeeModel import Employee
from models.employee_companyModel import EmployeeCompany
from models.contract_typeModel import ContractType

class Service:

    #Employee

    @classmethod
    def get_all(cls):
        return EmployeeDto.get_all()

    @classmethod
    def get_by_id(cls, id_dipendente : str):
        return EmployeeDto.get_by_id(id_dipendente)

    @classmethod
    def remove_by_id(cls, id_dipendente: str):
        return EmployeeDto.delete_by_id(id_dipendente)

    @classmethod
    def update_by_id(cls, id_dipendente, item):
        return EmployeeDto.put(id_dipendente, item)
    
    @classmethod
    def create(cls, item):
        return EmployeeDto.post(item)


    #Employee-company    

    @classmethod
    def get_all(cls):
        return EmployeeCompanyDto.get_all()

    @classmethod
    def get_employee_id(cls, id_dipendente : str):
        return EmployeeCompanyDto.get_employee_id(id_dipendente)

    @classmethod
    def get_company_id(cls, id_azienda : str):
        return EmployeeCompanyDto.get_company_id(id_azienda)    

    @classmethod
    def remove_by_employee_id(cls, id_dipendente: str):
        return EmployeeCompanyDto.delete_by_employee_id(id_dipendente)

    @classmethod
    def remove_by_company_id(cls, id_azienda: str):
        return EmployeeCompanyDto.delete_by_company_id(id_azienda)    

    @classmethod
    def update_by_employee_id(cls, id_dipendente, item):
        return EmployeeCompanyDto.put(id_dipendente, item)

    @classmethod
    def update_by_company_id(cls, id_azienda, item):
        return EmployeeCompanyDto.put(id_azienda, item)

    @classmethod
    def create(cls, item):
        return EmployeeCompanyDto.post(item)    


    #Contract-type   

    @classmethod
    def get_all(cls):
        return ContractTypeDto.get_all()

    @classmethod
    def get_by_id(cls, id_tipo_contratto : str):
        return ContractTypeDto.get_by_id(id_tipo_contratto)

    @classmethod
    def get_by_name(cls, nome_tipo_contratto : str):
        return ContractTypeDto.get_by_name(nome_tipo_contratto)    

    @classmethod
    def remove_by_id(cls, id_tipo_contratto: str):
        return ContractTypeDto.delete_by_id(id_tipo_contratto)

    @classmethod
    def remove_by_name(cls, nome_tipo_contratto: str):
        return ContractTypeDto.delete_by_name(nome_tipo_contratto)    

    @classmethod
    def update_by_id(cls, id_tipo_contratto, item):
        return ContractTypeDto.put(id_tipo_contratto, item)

    @classmethod
    def update_by_name(cls, nome_tipo_contratto, item):
        return ContractTypeDto.put(nome_tipo_contratto, item)

    @classmethod
    def create(cls, item):
        return ContractTypeDto.post(item)        