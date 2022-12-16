
from dao.assignmentDao import AssignmentDao
from models.assignment import Assignment

class AssignmentDto:
    
    @classmethod
    def get_all(cls):
        assignments = []
        res = AssignmentDao.find_all()
        for assignment in res:
            assignments.append(Assignment(**assignment))
        return assignments

    @classmethod
    def get_by_id(cls, id_commessa: str):
        res = AssignmentDao.find_by_id(id_commessa)
        return res

    @classmethod
    def post(cls, item: Assignment):
        AssignmentDao.create(item)

    @classmethod
    def put(cls, id_commessa: str, item: Assignment):
        AssignmentDao.update_by_id(id_commessa, item)

    @classmethod
    def delete(cls, id_commessa: str):
        AssignmentDao.remove_by_id(id_commessa)

