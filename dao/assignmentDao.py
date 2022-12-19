from utils.db import MySql
from models.assignment import Assignment

class AssignmentDao:
    
    @classmethod
    def find_all(cls):
        MySql.open_connection()
        MySql.query("SELECT * FROM commessa")
        res = MySql.get_results()
        MySql.close_connection()
        return res
    
    @classmethod
    def find_by_id(cls, id: str):
        MySql.open_connection()
        MySql.query(f"SELECT * FROM commessa WHERE id_commessa = '{id}'")
        res = MySql.get_result()
        MySql.close_connection()
        return res
    
    @classmethod
    def create(cls, Assignment: Assignment):
        MySql.open_connection()
        MySql.query(
            f"INSERT INTO commessa (id_commessa, descrizione, id_cliente, id_azienda, data_inizio, data_fine) \
            VALUES ('{Assignment.id_commessa}', IF('{Assignment.descrizione}' = 'NULL', NULL, '{Assignment.descrizione}'), '{Assignment.id_cliente}', '{Assignment.id_azienda}', '{Assignment.data_inizio}', '{Assignment.data_fine}')"
        )
        MySql.close_connection_commit()

    @classmethod
    def update_by_id(cls, id: str , Assignment: Assignment):
        MySql.open_connection()
        MySql.query(
            f"UPDATE commessa SET descrizione = IF('{Assignment.descrizione}' = 'NULL', NULL, '{Assignment.descrizione}'), id_cliente = '{Assignment.id_cliente}', id_azienda = '{Assignment.id_azienda}', data_inizio = '{Assignment.data_inizio}', data_fine = '{Assignment.data_fine}' \
                WHERE id_commessa = '{id}'"
        )
        MySql.close_connection_commit()

    @classmethod
    def remove_by_id(cls, id: str):
        MySql.open_connection()
        MySql.query(f"DELETE FROM commessa WHERE id_commessa = '{id}'")
        MySql.close_connection_commit()

