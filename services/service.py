
from dto.assignmentDto import AssignmentDto
from models.assignment import Assignment


class Service:

    @classmethod
    def get_all_assignments_service(cls):
        return AssignmentDto.get_all()
    
    @classmethod
    def get_assignment_by_id_service(cls, id_commessa: str):
        return AssignmentDto.get_by_id(id_commessa)
    
    @classmethod
    def post_assignment_service(cls, Assignment: Assignment):
        return AssignmentDto.post(Assignment)
        
    @classmethod
    def put_assignment_service(cls, id_commessa: str, Assignment: Assignment):
        return AssignmentDto.put(id_commessa, Assignment)
    
    @classmethod
    def delete_assignment_service(cls, id_commessa: str):
        return AssignmentDto.delete(id_commessa)
    
    
