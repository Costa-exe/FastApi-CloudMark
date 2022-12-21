from utils.db import MySql
from models.assignmentEmployee import AssignmentEmployee

class AssignmentEmployeeDao:
    
    @classmethod
    def find_all(cls):
        MySql.open_connection()
        MySql.query("SELECT * FROM commessa_dipendente")
        res = MySql.get_results()
        MySql.close_connection()
        return res
    
    @classmethod
    def find_specific(cls, id1 : str, id2 : str):
        MySql.open_connection()
        MySql.query(f"SELECT * FROM commessa_dipendente WHERE id_commessa = '{id1}' and id_dipendente = '{id2}'")
        result = MySql.get_result()
        MySql.close_connection()
        return result
    
    @classmethod
    def find_by_assignment_id(cls, id: str):
        MySql.open_connection()
        MySql.query(f"SELECT * FROM commessa_dipendente WHERE id_commessa = '{id}'")
        res = MySql.get_results()
        MySql.close_connection()
        return res
    
    @classmethod
    def find_by_employee_id(cls, id: str):
        MySql.open_connection()
        MySql.query(f"SELECT * FROM commessa_dipendente WHERE id_dipendente = '{id}'")
        res = MySql.get_results()
        MySql.close_connection()
        return res
    
    @classmethod
    def create(cls, AssignmentEmployee: AssignmentEmployee):
        MySql.open_connection()
        MySql.query(
            f"INSERT INTO commessa_dipendente (id_commessa, id_dipendente, rate) \
            VALUES ('{AssignmentEmployee.id_commessa}', '{AssignmentEmployee.id_dipendente}', '{AssignmentEmployee.rate}')"
        )
        MySql.close_connection_commit()
        
    @classmethod
    def update(cls, id1 : str, id2 : str, item : AssignmentEmployee):
        MySql.open_connection()
        MySql.query(f"""
                    UPDATE commessa_dipendente
                    SET
                    id_commessa = '{item.id_commessa}',
                    id_dipendente = '{item.id_dipendente}',
                    rate = '{item.rate}'
                    WHERE id_commessa = '{id1}' and id_dipendente = '{id2}'
                    """)
        MySql.close_connection_commit()
        
    @classmethod
    def remove_specific(cls, id1 : str, id2 : str):
        MySql.open_connection()
        MySql.query(f"DELETE FROM commessa_dipendente WHERE id_commessa = '{id1}' and id_dipendente = '{id2}'")
        MySql.close_connection_commit()
        
    @classmethod
    def remove_by_assignment_id(cls, id: str):
        MySql.open_connection()
        MySql.query(f"DELETE FROM commessa_dipendente WHERE id_commessa = '{id}'")
        MySql.close_connection_commit()
        
    @classmethod
    def remove_by_employee_id(cls, id: str):
        MySql.open_connection()
        MySql.query(f"DELETE FROM commessa_dipendente WHERE id_dipendente = '{id}'")
        MySql.close_connection_commit()

