from dao.employeeDao import EmployeeDao
from models.employeeModel import Employee

class EmployeeDto:

    @classmethod
    def get_all(cls):
        Employees = []
        results = EmployeeDao.find_all()
        for result in results:
                Employee.append(Employee(**result))
        return Employees

    @classmethod
    def get_by_id(cls, id : str):
        result = EmployeeDao.find_by_id(id)
        return Employee(**result)

    @classmethod
    def delete_by_id(cls, id : str):
        return EmployeeDao.remove_by_id(id)

    @classmethod
    def post(cls, item : Employee):
        return EmployeeDao.create(item)

    @classmethod
    def put(cls, id :str , item : Employee):
        return EmployeeDao.update_by_id(id, item)



