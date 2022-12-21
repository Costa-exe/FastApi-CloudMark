from utils.db import MySql
from models.contractTypeModel import ContractType

class ContractTypeDao:
    
    @classmethod
    def find_all(cls):
        MySql.open_connection()
        MySql.query("SELECT * FROM tipo_contratto")
        results = MySql.get_results()
        MySql.close_connection()
        return results

    @classmethod
    def find_by_id(cls, id :str):
        MySql.open_connection()
        MySql.query(f"SELECT * FROM tipo_contratto WHERE id_tipo_contratto = '{id}'")
        results = MySql.get_results()
        MySql.close_connection()
        return results

    @classmethod
    def find_by_name(cls, name : str):
        MySql.open_connection()
        MySql.query(f"SELECT * FROM tipo_contratto WHERE nome_tipo_contratto = '{name}'")
        results = MySql.get_results()
        MySql.close_connection()
        return results

    @classmethod
    def find_specific(cls, id1 : str, id2 : str):
        MySql.open_connection()
        MySql.query(f"SELECT * FROM tipo_contratto WHERE id_tipo_contratto = '{id1}' and nome_tipo_contratto = '{id2}'")
        result = MySql.get_result()
        MySql.close_connection()
        return result

    @classmethod
    def remove_by_id(cls, id : str):
        MySql.open_connection()
        MySql.query(f"DELETE FROM tipo_contratto WHERE id_tipo_contratto = '{id}'")
        MySql.close_connection_commit()

    @classmethod
    def remove_by_name(cls, name : str):
        MySql.open_connection()
        MySql.query(f"DELETE FROM tipo_contratto WHERE nome_tipo_contratto = '{name}'")
        MySql.close_connection_commit()

    @classmethod
    def remove_specific(cls, id1 : str, id2 : str):
        MySql.open_connection()
        MySql.query(f"DELETE FROM tipo_contratto WHERE id_tipo_contratto = '{id1}' and nome_tipo_contratto = '{id2}'")
        MySql.close_connection_commit()

    @classmethod
    def update(cls, id1 : str, id2 : str, item : ContractType):
        MySql.open_connection()
        MySql.query(f"""
                    UPDATE tipo_contratto
                    SET
                    id_tipo_contratto = '{item.id_tipo_contratto}',
                    nome_tipo_contratto = '{item.nome_tipo_contratto}',
                    descrizione = IF('{item.descrizione}' = 'NULL', NULL, '{item.descrizione}')
                    WHERE id_tipo_contratto = '{id1}' and nome_tipo_contratto = '{id2}'
                    """)
        MySql.close_connection_commit()
    

    @classmethod
    def create(cls, item : ContractType):
        MySql.open_connection()
        MySql.query(f"""
                    INSERT INTO tipo_contratto
                    (
                     id_tipo_contratto,
                     nome_tipo_contratto,
                     descrizione)
                    VALUES
                    ('{item.id_tipo_contratto}',
                     '{item.nome_tipo_contratto}',
                    IF('{item.descrizione}' = '', NULL, '{item.descrizione}'))
                    """)
        MySql.close_connection_commit()
    


   