from utils.db import MySql
from models.companyClientModel import CompanyClient

class CompanyClientDao:

    @classmethod
    def find_all(cls):
        MySql.open_connection()
        MySql.query("SELECT * FROM azienda_cliente")
        results = MySql.get_results()
        MySql.close_connection()
        return results

    @classmethod
    def find_by_client_id(cls, id : str):
        MySql.open_connection()
        MySql.query(f"SELECT * FROM azienda_cliente WHERE id_cliente = '{id}'")
        results = MySql.get_results()
        MySql.close_connection()
        return results
    
    @classmethod
    def find_by_company_id(cls, id : str):
        MySql.open_connection()
        MySql.query(f"SELECT * FROM azienda_cliente WHERE id_azienda = '{id}'")
        results = MySql.get_results()
        MySql.close_connection()
        return results

    @classmethod
    def find_specific(cls, id1 : str, id2 : str):
        MySql.open_connection()
        MySql.query(f"SELECT * FROM azienda_cliente WHERE id_azienda = '{id1}' and id_cliente = '{id2}'")
        result = MySql.get_result()
        MySql.close_connection()
        return result

    @classmethod
    def remove_by_client_id(cls, id : str):
        MySql.open_connection()
        MySql.query(f"DELETE FROM azienda_cliente WHERE id_cliente = '{id}'")
        MySql.close_connection_commit()

    @classmethod
    def remove_by_company_id(cls, id : str):
        MySql.open_connection()
        MySql.query(f"DELETE FROM azienda_cliente WHERE id_azienda = '{id}'")
        MySql.close_connection_commit()

    @classmethod
    def remove_specific(cls, id1 : str, id2 : str):
        MySql.open_connection()
        MySql.query(f"DELETE FROM azienda_cliente WHERE id_azienda = '{id1}' and id_cliente = '{id2}'")
        MySql.close_connection_commit()

    @classmethod
    def update(cls, id1 : str, id2 : str, item : CompanyClient):
        MySql.open_connection()
        MySql.query(f"""
                    UPDATE azienda_cliente
                    SET
                    id_azienda = '{item.id_azienda}',
                    id_cliente = '{item.id_cliente}'
                    WHERE id_azienda = '{id1}' and id_cliente = '{id2}'
                    """)
        MySql.close_connection_commit()

    @classmethod
    def create(cls, item : CompanyClient):
        MySql.open_connection()
        MySql.query(f"""
                    INSERT INTO azienda_cliente
                    (
                     id_azienda,
                     id_cliente)
                    VALUES
                    ('{item.id_azienda}',
                    '{item.id_cliente}'
                     )
                    """)
        MySql.close_connection_commit()
