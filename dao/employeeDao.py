from utils.db import MySql
from models.employeeModel import Employee

class EmployeeDao:


    @classmethod
    def find_all(cls):
        MySql.open_connection()
        MySql.query("SELECT * FROM dipendente")
        results = MySql.get_results()
        MySql.close_connection()
        return results

    @classmethod
    def find_by_id(cls, id :str):
        MySql.open_connection()
        MySql.query(f"SELECT * FROM dipendente WHERE id_dipendente = '{id}'")
        results = MySql.get_results()
        MySql.close_connection()
        return results

    @classmethod
    def remove_by_id(cls, id :str):
        MySql.open_connection()
        MySql.query(f"DELETE FROM dipendente WHERE id_dipendente = '{id}'")
        MySql.close_connection_commit()

    @classmethod
    def update_by_id(cls, id :str, item : Employee):
        MySql.open_connection()
        MySql.query(f"""
                    UPDATE cliente
                    SET                                                                 
                    id_dipendente = '{item.id_dipendente}',
                    nome = IF('{item.nome}' = '', NULL, '{item.nome}'),
                    cognome = IF('{item.cognome}' = '', NULL, '{item.cognome}'),
                    cf = '{item.cf}',                   
                    iban = '{item.iban}',
                    email = IF('{item.email}' = '', NULL, '{item.email}'),
                    telefono = IF('{item.telefono}' = '', NULL, '{item.telefono}'),
                    id_tipo_contratto = '{item.id_tipo_contratto}'
                    WHERE id_cliente = '{id}'
                    """)
        MySql.close_connection_commit()

    @classmethod
    def create(cls, item : Employee):
        MySql.open_connection()
        MySql.query(f"""
                    INSERT INTO dipendente
                    (
                     id_dipendente,
                     nome,
                     cognome,
                     cf,
                     iban,
                     telefono,
                     email,
                     id_tipo_contratto
                     )
                    VALUES
                    ('{item.id_dipendente}',
                    IF('{item.nome}' = '', NULL, '{item.nome}'),
                    IF('{item.cognome}' = '', NULL, '{item.cognome}'),
                     '{item.cf}',
                     '{item.iban}',
                    IF('{item.telefono}' = '', NULL, '{item.telefono}'),
                    IF('{item.email}' = '', NULL, '{item.email}'),
                     '{item.id_tipo_contratto}')
                    """)
        MySql.close_connection_commit()

    