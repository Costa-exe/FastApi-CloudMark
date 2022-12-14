from dto.employeeDto import EmployeeDto
from dto.employee_companyDto import EmployeeCompanyDto
from dto.contract_typeDto import ContractTypeDto

class Service:

    #Employee

    @classmethod
    def getAllEmployee(cls):
        return EmployeeDto.getAllEmployee()

    @classmethod
    def getById(cls, id_dipendente : str):
        return EmployeeDto.getById(id_dipendente)

    @classmethod
    def DeleteById(cls, id_dipendente: str):
        return EmployeeDto.DeleteById(id_dipendente)

    @classmethod
    def createNew(cls, item):
        return EmployeeDto.post(item)

    @classmethod
    def updateById(cls, id_dipendente, item):
        return EmployeeDto.put(id_dipendente, item)

    #Employee-company    

    @classmethod
    def getAllEmployee_company(cls):
        return EmployeeCompanyDto.getAllEmployee_company()

    @classmethod
    def getEmployeeId(cls, id_dipendente : str):
        return EmployeeCompanyDto.getEmployeeId(id_dipendente)

    @classmethod
    def getCompanyId(cls, id_azienda : str):
        return EmployeeCompanyDto.getCompanyId(id_azienda)    

    @classmethod
    def DeleteById(cls, id_dipendente: str):
        return EmployeeCompanyDto.DeleteById(id_dipendente)

    @classmethod
    def DeleteByName(cls, id_azienda: str):
        return EmployeeCompanyDto.DeleteById(id_azienda)    

    @classmethod
    def updateByEmployeeId(cls, id_dipendente, item):
        return EmployeeCompanyDto.put(id_dipendente, item)

    @classmethod
    def updateByCompanyId(cls, id_azienda, item):
        return EmployeeCompanyDto.put(id_azienda, item)

    @classmethod
    def createNew(cls, item):
        return EmployeeCompanyDto.post(item)    


    #Contract-type   

    @classmethod
    def getAllEmployee(cls):
        return ContractTypeDto.getAllEmployee()

    @classmethod
    def getById(cls, id_tipo_contratto : str):
        return ContractTypeDto.getById(id_tipo_contratto)

    @classmethod
    def getByName(cls, nome_tipo_contratto : str):
        return ContractTypeDto.getByName(nome_tipo_contratto)    

    @classmethod
    def DeleteById(cls, id_tipo_contratto: str):
        return ContractTypeDto.DeleteById(id_tipo_contratto)

    @classmethod
    def DeleteByName(cls, nome_tipo_contratto: str):
        return ContractTypeDto.DeleteById(nome_tipo_contratto)    

    @classmethod
    def updateById(cls, id_tipo_contratto, item):
        return ContractTypeDto.put(id_tipo_contratto, item)

    @classmethod
    def updateByName(cls, nome_tipo_contratto, item):
        return ContractTypeDto.put(nome_tipo_contratto, item)

    @classmethod
    def createNew(cls, item):
        return ContractTypeDto.post(item)        