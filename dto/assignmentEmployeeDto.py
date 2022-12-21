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
    def get_specific(cls, id1 : str, id2 : str):
        result = AssignmentEmployeeDao.find_specific(id1, id2)
        return result

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
    def put(cls, id1 : str, id2 : str, item : AssignmentEmployee):
        return AssignmentEmployeeDao.update(id1, id2, item)
        
    @classmethod
    def delete_by_assignment_id(cls, id: str):
        AssignmentEmployeeDao.remove_by_assignment_id(id)
        
    @classmethod
    def delete_by_employee_id(cls, id: str):
        AssignmentEmployeeDao.remove_by_employee_id(id)
        
    @classmethod
    def delete_specific(cls, id1 : str, id2 : str):
        return AssignmentEmployeeDao.remove_specific(id1, id2)
