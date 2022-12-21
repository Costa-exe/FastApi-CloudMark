from dao.employeeCompanyDao import EmployeeCompanyDao
from models.employeeCompanyModel import EmployeeCompany

class EmployeeCompanyDto:

    @classmethod
    def get_all(cls):
        EmployeesCompanies = []
        results = EmployeeCompanyDao.find_all()
        for result in results:
                EmployeesCompanies.append(EmployeeCompany(**result))
        return EmployeesCompanies

    @classmethod
    def get_by_employee_id(cls, id : str):
        employees_companies = []
        result = EmployeeCompanyDao.find_by_employee_id(id)
        for r in result:
            employees_companies.append(EmployeeCompany(**r))
        return employees_companies

    @classmethod
    def get_by_company_id(cls, id : str):
        employees_companies = [] 
        result = EmployeeCompanyDao.find_by_company_id(id)
        for r in result:
            employees_companies.append(EmployeeCompany(**r))
        return employees_companies

    @classmethod
    def get_specific(cls, id1 : str, id2 : str):
        result = EmployeeCompanyDao.find_specific(id1, id2)
        return result

    @classmethod
    def delete_by_employee_id(cls, id : str):
        return EmployeeCompanyDao.remove_by_employee_id(id)

    @classmethod
    def delete_by_company_id(cls, id : str):
        return EmployeeCompanyDao.remove_by_company_id(id)

    @classmethod
    def delete_specific(cls, id1 : str, id2 : str):
        return EmployeeCompanyDao.remove_specific(id1, id2)

    @classmethod
    def put(cls, id1 : str, id2 : str, item : EmployeeCompany):
        return EmployeeCompanyDao.update(id1, id2, item)

    @classmethod
    def post(cls, item : EmployeeCompany):
        return EmployeeCompanyDao.create(item)

