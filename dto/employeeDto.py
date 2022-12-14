from dao.employeeDao import EmployeeDao
from models.employeeModel import Employee

class EmployeeDto:

    @classmethod
    def getAllEmployee(cls):
        Employee = []
        results = EmployeeDao.findAllEmployee()
        for result in results:
                Employee.append(Employee(**result))
        return Employee

    @classmethod
    def getById(cls, id_dipendente : str):
        result = EmployeeDao.findById(id_dipendente)
        return Employee(**result[0])

    @classmethod
    def DeleteById(cls, id_dipendente : str):
        return EmployeeDao.removeById(id_dipendente)

    @classmethod
    def post(cls, item):
        return EmployeeDao.createNew(item)

    @classmethod
    def put(cls, id_dipendente, item):
        return EmployeeDao.updateById(id_dipendente, item)



