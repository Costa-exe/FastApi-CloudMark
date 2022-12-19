from dao.employeeDao import EmployeeDao
from models.employeeModel import Employee

class EmployeeDto:

    @classmethod
    def get_all(cls):
        Employee = []
        results = EmployeeDao.find_all()
        for result in results:
                Employee.append(result)
        return Employee

    @classmethod
    def get_by_id(cls, id_dipendente : str):
        result = EmployeeDao.find_by_id(id_dipendente)
        return result

    @classmethod
    def delete_by_id(cls, id_dipendente : str):
        return EmployeeDao.remove_by_id(id_dipendente)

    @classmethod
    def post(cls, item : Employee):
        return EmployeeDao.create(item)

    @classmethod
    def put(cls, id_dipendente :str , item : Employee):
        return EmployeeDao.update_by_id(id_dipendente, item)



