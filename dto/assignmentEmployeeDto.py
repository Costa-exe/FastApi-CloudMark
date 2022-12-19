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
    def get_by_assignment_id(cls, id: str):
        res = AssignmentEmployeeDao.find_by_assignment_id(id)
        return AssignmentEmployee(**res)
    
    @classmethod
    def get_by_employee_id(cls, id: str):
        res = AssignmentEmployeeDao.find_by_employee_id(id)
        return AssignmentEmployee(**res)

    @classmethod
    def post(cls, item: AssignmentEmployee):
        AssignmentEmployeeDao.create(item)

    @classmethod
    def put_by_assignment_id(cls, id: str, item: AssignmentEmployee):
        AssignmentEmployeeDao.update_by_assignment_id(id, item)
        
    @classmethod
    def put_by_employee_id(cls, id: str, item: AssignmentEmployee):
        AssignmentEmployeeDao.update_by_employee_id(id, item)
        
    @classmethod
    def delete_by_assignment_id(cls, id: str):
        AssignmentEmployeeDao.remove_by_assignment_id(id)
        
    @classmethod
    def delete_by_employee_id(cls, id: str):
        AssignmentEmployeeDao.remove_by_employee_id(id)
