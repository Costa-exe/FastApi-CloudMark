from dao.employee_companyDao import EmployeeCompanyDao
from models.employee_companyModel import EmployeeCompany

class EmployeeCompanyDto:

    @classmethod
    def getAllEmployee_company(cls):
        EmployeeCompany = []
        results = EmployeeCompanyDao.findAllEmployee_company()
        for result in results:
                EmployeeCompany.append(result)
        return EmployeeCompany

    @classmethod
    def getEmployeeId(cls, id_dipendente : str):
        result = EmployeeCompanyDao.findEmployeeId(id_dipendente)
        return result

    @classmethod
    def getCompanyId(cls, id_azienda : str):
        result = EmployeeCompanyDao.findEmployeeId(id_azienda)
        return result

    @classmethod
    def DeleteByEmployeeId(cls, id_dipendente : str):
        return EmployeeCompanyDao.removeByEmployeeId(id_dipendente)

    @classmethod
    def DeleteByCompanyId(cls, id_azienda : str):
        return EmployeeCompanyDao.removeByCompanyId(id_azienda)

    @classmethod
    def put(cls, id_dipendente :str, item : EmployeeCompany):
        return EmployeeCompanyDao.updateByEmployeeId(id_dipendente, item)

    @classmethod
    def put(cls, id_azienda :str , item : EmployeeCompany):
        return EmployeeCompanyDao.updateByCompanyId(id_azienda, item)

    @classmethod
    def post(cls, item : EmployeeCompany):
        return EmployeeCompanyDao.createNew(item)    


