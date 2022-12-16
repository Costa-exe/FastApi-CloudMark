from dao.assignmentEmployeeDao import AssignmentEmployeeDao
from models.assignmentEmployee import AssignmentEmployee

class AssignmentEmployeeDto:
    
    @classmethod
    def get_all(cls):
        assignments = []
        res = AssignmentEmployeeDao.find_all()
        for assignment in res:
            assignments.append(AssignmentEmployee(**assignment))
        return assignments

    @classmethod
    def get_by_assignment_id(cls, id_commessa: str):
        res = AssignmentEmployeeDao.find_by_assignment_id(id_commessa)
        return res
    
    @classmethod
    def get_by_employee_id(cls, id_dipendente: str):
        res = AssignmentEmployeeDao.find_by_employee_id(id_dipendente)
        return res

    @classmethod
    def post(cls, item: AssignmentEmployee):
        AssignmentEmployeeDao.create(item)

    @classmethod
    def put_by_assignment_id(cls, id_commessa: str, item: AssignmentEmployee):
        AssignmentEmployeeDao.update_by_assignment_id(id_commessa, item)
        
    @classmethod
    def put_by_employee_id(cls, id_dipendente: str, item: AssignmentEmployee):
        AssignmentEmployeeDao.update_by_employee_id(id_dipendente, item)
        
    @classmethod
    def delete_by_assignment_id(cls, id_commessa: str):
        AssignmentEmployeeDao.remove_by_assignment_id(id_commessa)
        
    @classmethod
    def delete_by_employee_id(cls, id_dipendente: str):
        AssignmentEmployeeDao.remove_by_employee_id(id_dipendente)
