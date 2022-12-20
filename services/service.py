from dto.companyDto import CompanyDto
from dto.clientDto import ClientDto
from dto.companyClientDto import CompanyClientDto
from dto.assignmentDto import AssignmentDto
from dto.assignmentEmployeeDto import AssignmentEmployeeDto
from dto.employeeDto import EmployeeDto
from dto.employeeCompanyDto import EmployeeCompanyDto
from dto.contractTypeDto import ContractTypeDto
from models.clientModel import Client
from models.companyModel import Company
from models.companyClientModel import CompanyClient
from models.assignment import Assignment
from models.assignmentEmployee import AssignmentEmployee
from models.employeeModel import Employee
from models.employeeCompanyModel import EmployeeCompany
from models.contractTypeModel import ContractType

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
    def get_all_employees(cls):
        return EmployeeDto.get_all()

    @classmethod
    def get_employee_by_id(cls, id : str):
        return EmployeeDto.get_by_id(id)

    @classmethod
    def remove_employee_by_id(cls, id: str):
        return EmployeeDto.delete_by_id(id)

    @classmethod
    def update_employee_by_id(cls, id, item : Employee):
        return EmployeeDto.put(id, item)
    
    @classmethod
    def create_employee(cls, item : Employee):
        return EmployeeDto.post(item)


    #Employee-company    

    @classmethod
    def get_all_employee_company(cls):
        return EmployeeCompanyDto.get_all()

    @classmethod
    def get_employee_company_by_employee_id(cls, id : str):
        return EmployeeCompanyDto.get_by_employee_id(id)

    @classmethod
    def get_employee_company_by_company_id(cls, id : str):
        return EmployeeCompanyDto.get_by_company_id(id)    

    @classmethod
    def remove_employee_company_by_employee_id(cls, id: str):
        return EmployeeCompanyDto.delete_by_employee_id(id)

    @classmethod
    def remove_employee_company_by_company_id(cls, id: str):
        return EmployeeCompanyDto.delete_by_company_id(id)    

    @classmethod
    def update_employee_company_by_employee_id(cls, id, item : EmployeeCompany):
        return EmployeeCompanyDto.put_by_employee_id(id, item)

    @classmethod
    def update_employee_company_by_company_id(cls, id, item : EmployeeCompany):
        return EmployeeCompanyDto.put_by_company_id(id, item)

    @classmethod
    def create_employee_company(cls, item : EmployeeCompany):
        return EmployeeCompanyDto.post(item)    

    #Contract-type   

    @classmethod
    def get_all_contract_type(cls):
        return ContractTypeDto.get_all()

    @classmethod
    def get_contract_type_by_id(cls, id : str):
        return ContractTypeDto.get_by_id(id)

    @classmethod
    def get_contract_type_by_name(cls, nome : str):
        return ContractTypeDto.get_by_name(nome)    

    @classmethod
    def remove_contract_type_by_id(cls, id: str):
        return ContractTypeDto.delete_by_id(id)

    @classmethod
    def remove_contract_type_by_name(cls, nome: str):
        return ContractTypeDto.delete_by_name(nome)    

    @classmethod
    def update_contract_type_by_id(cls, id, item : ContractType):
        return ContractTypeDto.put_by_id(id, item)

    @classmethod
    def update_contract_type_by_name(cls, nome, item : ContractType):
        return ContractTypeDto.put_by_name(nome, item)

    @classmethod
    def create_contract_type(cls, item : ContractType):
        return ContractTypeDto.post(item)        
