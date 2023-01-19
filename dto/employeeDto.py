from dao.employeeDao import EmployeeDao
from models.employeeModel import Employee
import csv
from models.customEmployeeModel import CustomEmployee
import os


class EmployeeDto:

    @classmethod
    def get_csv(cls, items: list[CustomEmployee]):
        fieldnames = ['cognome', 'nome',
                      'matricola', 'contratto', 'assunzione']
        with open('dipendenti.csv', 'w', encoding='UTF8', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for item in items:
                writer.writerow(item.dict())

    @classmethod
    def delete_csv(cls):
        os.remove('./dipendenti.csv')
        return 'File Scaricato Con Successo'

    @classmethod
    def get_all(cls):
        Employees = []
        results = EmployeeDao.find_all()
        for result in results:
            Employees.append(Employee(**result))
        return Employees

    @classmethod
    def get_by_name_surname(cls, name: str):
        Employees = []
        results = EmployeeDao.find_by_name_surname(name)
        for result in results:
            Employees.append(result)
        return Employees

    @classmethod
    def get_by_multi(cls, value: str, id: str):
        Employees = []
        results = EmployeeDao.find_by_multi(value, id)
        for result in results:
            Employees.append(result)
        return Employees

    @classmethod
    def get_by_multi_active(cls, value: str, id: str):
        Employees = []
        results = EmployeeDao.find_by_multi_active(value, id)
        for result in results:
            Employees.append(result)
        return Employees

    @classmethod
    def get_all_inactive(cls, id: str):
        Employees = []
        results = EmployeeDao.find_all_inactive(id)
        for result in results:
            Employees.append(result)
        return Employees

    @classmethod
    def get_all_active(cls, id: str):
        Employees = []
        results = EmployeeDao.find_all_active(id)
        for result in results:
            Employees.append(result)
        return Employees

    @classmethod
    def get_full_details(cls, id: str):
        results = EmployeeDao.find_full_details(id)
        return results

    @classmethod
    def get_info_assignments(cls, id: str):
        result = EmployeeDao.find_info_assignments(id)
        return result

    @classmethod
    def get_by_id(cls, id: str):
        result = EmployeeDao.find_by_id(id)
        return result

    @classmethod
    def delete_by_id(cls, id: str):
        return EmployeeDao.remove_by_id(id)

    @classmethod
    def post(cls, item: Employee):
        return EmployeeDao.create(item)

    @classmethod
    def put(cls, id: str, item: Employee):
        return EmployeeDao.update_by_id(id, item)
