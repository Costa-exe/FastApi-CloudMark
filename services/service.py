from dto.companyDto import CompanyDto
from dto.clientDto import ClientDto
from dto.companyClientDto import CompanyClientDto
from dto.assignmentDto import AssignmentDto
from dto.assignmentEmployeeDto import AssignmentEmployeeDto
from dto.employeeDto import EmployeeDto
from dto.employee_companyDto import EmployeeCompanyDto
from dto.contract_typeDto import ContractTypeDto
from models.clientModel import Client
from models.companyModel import Company
from models.companyClientModel import CompanyClient
from models.assignment import Assignment
from models.assignmentEmployee import AssignmentEmployee
from models.employeeModel import Employee
from models.employee_companyModel import EmployeeCompany
from models.contract_typeModel import ContractType

class Service:

    #companies services

    @classmethod
    def get_all_companies_service(cls):
        return CompanyDto.get_all()

    @classmethod
    def get_company_by_id_service(cls, id : str):
        return CompanyDto.get_by_id(id)

    @classmethod
    def delete_company_by_id_service(cls, id : str):
        return CompanyDto.delete(id)

    @classmethod
    def create_new_company(cls, item : Company):
        return CompanyDto.post(item)

    @classmethod
    def update_company(cls, id : str, item : Company):
        return CompanyDto.put(id, item)

    #clients services    

    @classmethod
    def get_all_clients_service(cls):
        return ClientDto.get_all()

    @classmethod
    def get_client_by_id_service(cls, id : str):
        return ClientDto.get_by_id(id)

    @classmethod
    def delete_client_by_id_service(cls, id : str):
        return ClientDto.delete(id)

    @classmethod
    def create_new_client(cls, item : Client):
        return ClientDto.post(item)

    @classmethod
    def update_client(cls, id : str, item : Client):
        return ClientDto.put(id, item)

    #company_client services

    @classmethod
    def get_all_company_client_service(cls):
        return CompanyClientDto.get_all()

    @classmethod
    def get_company_client_by_client_id_service(cls, id : str):
        return CompanyClientDto.get_by_client_id(id)

    @classmethod
    def get_company_client_by_company_id_service(cls, id : str):
        return CompanyClientDto.get_by_company_id(id)

    @classmethod
    def delete_company_client_by_client_id_service(cls, id: str):
        return CompanyClientDto.delete_by_client_id(id)

    @classmethod
    def delete_company_client_by_company_id_service(cls, id : str):
        return CompanyClientDto.delete_by_company_id(id)

    @classmethod
    def create_new_company_client(cls, item : CompanyClient):
        return CompanyClientDto.post(item)

    @classmethod
    def update_company_client_by_client_id(cls, id : str, item : CompanyClient):
        return CompanyClientDto.put_by_client_id(id, item)
    
    @classmethod
    def update_company_client_by_company_id(cls, id : str, item : CompanyClient):
        return CompanyClientDto.put_by_company_id(id, item)
        
    # Assignment
    
    @classmethod
    def get_all_assignments_service(cls):
        return AssignmentDto.get_all()
    
    @classmethod
    def get_assignment_by_id_service(cls, id: str):
        return AssignmentDto.get_by_id(id)
    
    @classmethod
    def post_assignment_service(cls, item: Assignment):
        return AssignmentDto.post(item)
        
    @classmethod
    def put_assignment_service(cls, id: str, item: Assignment):
        return AssignmentDto.put(id, item)
    
    @classmethod
    def delete_assignment_service(cls, id: str):
        return AssignmentDto.delete(id)
    
    # Assignment Employee
    
    @classmethod
    def get_all_assignments_employee_service(cls):
        return AssignmentEmployeeDto.get_all()
    
    @classmethod
    def get_assignments_employee_by_assignment_id_service(cls, id: str):
        return AssignmentEmployeeDto.get_by_assignment_id(id)
    
    @classmethod
    def get_assignments_employee_by_employee_id_service(cls, id: str):
        return AssignmentEmployeeDto.get_by_employee_id(id)
    
    @classmethod
    def post_assignments_employee_service(cls, item: AssignmentEmployee):
        return AssignmentEmployeeDto.post(item)
    
    @classmethod
    def put_assignments_employee_by_assignment_id_service(cls, id: str, item: AssignmentEmployee):
        return AssignmentEmployeeDto.put_by_assignment_id(id, item)
    
    @classmethod
    def put_assignments_employee_by_employee_id_service(cls, id: str, item: AssignmentEmployee):
        return AssignmentEmployeeDto.put_by_employee_id(id, item)
    
    @classmethod
    def delete_assignments_employee_by_assignment_id_service(cls, id: str):
        return AssignmentEmployeeDto.delete_by_assignment_id(id)
    
    @classmethod
    def delete_assignments_employee_by_employee_id_service(cls, id: str):
        return AssignmentEmployeeDto.delete_by_employee_id(id)
     
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
