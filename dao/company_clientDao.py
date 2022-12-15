from utils.db import MySql
from models.company_clientModel import Company_Client

class Company_Client_dao:

    @classmethod
    def find_all(cls):
        MySql.openConnection()
        MySql.query("SELECT * FROM azienda_cliente")
        results = MySql.getResults()
        MySql.closeConnection()
        return results

    @classmethod
    def find_by_client_id(cls, id : str):
        MySql.openConnection()
        MySql.query(f"SELECT * FROM azienda_cliente WHERE id_cliente = '{id}'")
        results = MySql.getResult()
        MySql.closeConnection()
        return results
    
    @classmethod
    def find_by_company_id(cls, id : str):
        MySql.openConnection()
        MySql.query(f"SELECT * FROM azienda_cliente WHERE id_azienda = '{id}'")
        results = MySql.getResult()
        MySql.closeConnection()
        return results

    @classmethod
    def remove_by_client_id(cls, id : str):
        MySql.openConnection()
        MySql.query(f"DELETE FROM azienda_cliente WHERE id_cliente = '{id}'")
        MySql.closeConnectionCommit()
    
    @classmethod
    def remove_by_company_id(cls, id : str):
        MySql.openConnection()
        MySql.query(f"DELETE FROM azienda_cliente WHERE id_azienda = '{id}'")
        MySql.closeConnectionCommit()

    @classmethod
    def update_by_client_id(cls, id : str, item : Company_Client):
        MySql.openConnection()
        MySql.query(f"""
                    UPDATE azienda_cliente
                    SET
                    id_azienda = '{item.id_azienda}',
                    id_cliente = '{item.id_cliente}'
                    WHERE id_cliente = '{id}'
                    """)
        MySql.closeConnectionCommit()

    @classmethod
    def update_by_company_id(cls, id : str, item : Company_Client):
        MySql.openConnection()
        MySql.query(f"""
                    UPDATE azienda_cliente
                    SET
                    id_azienda = '{item.id_azienda}',
                    id_cliente = '{item.id_cliente}'
                    WHERE id_azienda = '{id}'
                    """)
        MySql.closeConnectionCommit()


    @classmethod
    def create_new(cls, item : Company_Client):
        MySql.openConnection()
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
        MySql.closeConnectionCommit()