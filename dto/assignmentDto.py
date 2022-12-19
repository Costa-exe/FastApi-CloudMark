
from dao.assignmentDao import AssignmentDao
from models.assignment import Assignment

class AssignmentDto:
    
    @classmethod
    def get_all(cls):
        assignments = []
        res = AssignmentDao.find_all()
        for assignment in res:
            assignments.append(assignment)
        return assignments

    @classmethod
    def get_by_id(cls, id: str):
        res = AssignmentDao.find_by_id(id)
        return res

    @classmethod
    def post(cls, item: Assignment):
        AssignmentDao.create(item)

    @classmethod
    def put(cls, id: str, item: Assignment):
        AssignmentDao.update_by_id(id, item)

    @classmethod
    def delete(cls, id: str):
        AssignmentDao.remove_by_id(id)

