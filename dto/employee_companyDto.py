from dao.employee_companyDao import EmployeeCompanyDao
from models.employee_companyModel import EmployeeCompany

class EmployeeCompanyDto:

    @classmethod
    def get_all(cls):
        EmployeeCompany = []
        results = EmployeeCompanyDao.find_all()
        for result in results:
                EmployeeCompany.append(result)
        return EmployeeCompany

    @classmethod
    def get_employee_id(cls, id_dipendente : str):
        result = EmployeeCompanyDao.find_by_employee_id(id_dipendente)
        return result

    @classmethod
    def get_company_id(cls, id_azienda : str):
        result = EmployeeCompanyDao.find_by_employee_id(id_azienda)
        return result

    @classmethod
    def delete_by_employee_id(cls, id_dipendente : str):
        return EmployeeCompanyDao.remove_by_employee_id(id_dipendente)

    @classmethod
    def delete_by_company_id(cls, id_azienda : str):
        return EmployeeCompanyDao.remove_by_company_id(id_azienda)

    @classmethod
    def put(cls, id_dipendente :str, item : EmployeeCompany):
        return EmployeeCompanyDao.update_by_employee_id(id_dipendente, item)

    @classmethod
    def put(cls, id_azienda :str , item : EmployeeCompany):
        return EmployeeCompanyDao.update_by_company_id(id_azienda, item)

    @classmethod
    def post(cls, item : EmployeeCompany):
        return EmployeeCompanyDao.create(item)    


