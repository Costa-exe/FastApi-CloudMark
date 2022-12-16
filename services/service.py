
from dto.assignmentDto import AssignmentDto
from dto.assignmentEmployeeDto import AssignmentEmployeeDto
from models.assignment import Assignment
from models.assignmentEmployee import AssignmentEmployee


class Service:

    # Assignment
    
    @classmethod
    def get_all_assignments_service(cls):
        return AssignmentDto.get_all()
    
    @classmethod
    def get_assignment_by_id_service(cls, id: str):
        return AssignmentDto.get_by_id(id)
    
    @classmethod
    def post_assignment_service(cls, item: Assignment):
        return AssignmentDto.post(item)
        
    @classmethod
    def put_assignment_service(cls, id: str, item: Assignment):
        return AssignmentDto.put(id, item)
    
    @classmethod
    def delete_assignment_service(cls, id: str):
        return AssignmentDto.delete(id)
    
    # Assignment Employee
    
    @classmethod
    def get_all_assignments_employee_service(cls):
        return AssignmentEmployeeDto.get_all()
    
    @classmethod
    def get_assignments_employee_by_assignment_id_service(cls, id: str):
        return AssignmentEmployeeDto.get_by_assignment_id(id)
    
    @classmethod
    def get_assignments_employee_by_employee_id_service(cls, id: str):
        return AssignmentEmployeeDto.get_by_employee_id(id)
    
    @classmethod
    def post_assignments_employee_service(cls, item: AssignmentEmployee):
        return AssignmentEmployeeDto.post(item)
    
    @classmethod
    def put_assignments_employee_by_assignment_id_service(cls, id: str, item: AssignmentEmployee):
        return AssignmentEmployeeDto.put_by_assignment_id(id, item)
    
    @classmethod
    def put_assignments_employee_by_employee_id_service(cls, id: str, item: AssignmentEmployee):
        return AssignmentEmployeeDto.put_by_employee_id(id, item)
    
    @classmethod
    def delete_assignments_employee_by_assignment_id_service(cls, id: str):
        return AssignmentEmployeeDto.delete_by_assignment_id(id)
    
    @classmethod
    def delete_assignments_employee_by_employee_id_service(cls, id: str):
        return AssignmentEmployeeDto.delete_by_employee_id(id)

