from utils.db import MySql
from models.employee_companyModel import EmployeeCompany

class EmployeeCompanyDao:
    
    @classmethod
    def find_all(cls):
        MySql.open_connection()
        MySql.query("SELECT * FROM dipendente_azienda")
        results = MySql.get_results()
        MySql.close_connection()
        return results

    @classmethod
    def find_by_employee_id(cls, id_dipendente :str):
        MySql.open_connection()
        MySql.query(f"SELECT * FROM dipendente_azienda WHERE id_dipendente = '{id_dipendente}'")
        results = MySql.get_results()
        MySql.close_connection()
        return results

    @classmethod
    def find_by_company_id(cls, id_azienda :str):
        MySql.open_connection()
        MySql.query(f"SELECT * FROM dipendente_azienda WHERE id_azienda = '{id_azienda}'")
        results = MySql.get_results()
        MySql.close_connection()
        return results

    @classmethod
    def remove_by_employee_id(cls, id_dipendente :str):
        MySql.open_connection()
        MySql.query(f"DELETE FROM dipendente_azienda WHERE id_dipendente = '{id_dipendente}'")
        MySql.close_connectionCommit()

    @classmethod
    def remove_by_company_id(cls, id_azienda :str):
        MySql.open_connection()
        MySql.query(f"DELETE FROM dipendente_azienda WHERE id_azienda = '{id_azienda}'")
        MySql.close_connectionCommit()

    @classmethod
    def update_by_employee_id(cls, id_dipendente :str, item : EmployeeCompany):
        MySql.open_connection()
        MySql.query(f"""
                    UPDATE dipendente_azienda
                    SET
                    id_dipendente = '{item.id_dipendente}',
                    id_azienda = '{item.id_azienda}',
                    data_inizio_rapporto = '{item.data_inizio_rapporto}',
                    matricola = IF('{item.matricola}' = '', NULL, '{item.matricola}'),
                    data_fine_raporto = IF('{item.data_fine_rapporto}' = '', NULL, '{item.data_fine_rapporto}'),
                    WHERE id_dipendente = '{id_dipendente}'
                    """)
        MySql.close_connectionCommit()

    @classmethod
    def update_by_company_id(cls, id_azienda :str, item : EmployeeCompany):
        MySql.open_connection()
        MySql.query(f"""
                    UPDATE dipendente_azienda
                    SET
                    id_dipendente = '{item.id_dipendente}',
                    id_azienda = '{item.id_azienda}',
                    data_inizio_rapporto = '{item.data_inizio_rapporto}',
                    matricola = IF('{item.matricola}' = '', NULL, '{item.matricola}'),
                    data_fine_raporto = IF('{item.data_fine_rapporto}' = '', NULL, '{item.data_fine_rapporto}')
                    WHERE id_azienda = '{id_azienda}'
                    """)
        MySql.close_connectionCommit()        

    @classmethod
    def create(cls, item : EmployeeCompany):
        MySql.open_connection()
        MySql.query(f"""
                    INSERT INTO dipendente_azienda
                    (
                     id_dipendente,
                     id_azienda,
                     data_inizio_rapporto,
                     matricola,
                     data_fine_rapporto
                    VALUES
                    ('{item.id_dipendente}',
                     '{item.id_azienda}',
                     '{item.data_inizio_rapporto}',
                    IF('{item.matricola}' = '', NULL, '{item.matricola}'),
                    IF('{item.data_fine_rapporto}' = '', NULL, '{item.data_fine_rapporto}')
                    """)
        MySql.close_connectionCommit()
    


   
    