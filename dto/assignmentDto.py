
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
    def post(cls, Assignment: Assignment):
        AssignmentDao.create(Assignment)

    @classmethod
    def put(cls, id_commessa: str, Assignment: Assignment):
        AssignmentDao.update(id_commessa, Assignment)

    @classmethod
    def delete(cls, id_commessa: str):
        AssignmentDao.remove_by_id(id_commessa)
