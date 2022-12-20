from utils.db import MySql
from models.clientModel import Client

class ClientDao:

    @classmethod
    def find_all(cls):
        MySql.open_connection()
        MySql.query("SELECT * FROM cliente")
        results = MySql.get_results()
        MySql.close_connection()
        return results

    @classmethod
    def find_by_id(cls, id : str):
        MySql.open_connection()
        MySql.query(f"SELECT * FROM cliente WHERE id_cliente = '{id}'")
        results = MySql.get_result()
        MySql.close_connection()
        return results

    @classmethod
    def remove_by_id(cls, id : str):
        MySql.open_connection()
        MySql.query(f"DELETE FROM cliente WHERE id_cliente = '{id}'")
        MySql.close_connection_commit()

    @classmethod
    def update_by_id(cls, id : str, item : Client):
        MySql.open_connection()
        MySql.query(f"""
                    UPDATE cliente
                    SET
                    id_cliente = '{item.id_cliente}',
                    nome = IF('{item.nome}' = '', NULL, '{item.nome}'),
                    p_iva = IF('{item.p_iva}' = '', NULL, '{item.p_iva}'),
                    indirizzo = IF('{item.indirizzo}' = '', NULL, '{item.indirizzo}'),
                    cap = IF('{item.cap}' = '', NULL, '{item.cap}'),
                    iban = IF('{item.iban}' = '', NULL, '{item.iban}'),
                    telefono = IF('{item.telefono}' = '', NULL, '{item.telefono}'),
                    email = IF('{item.email}' = '', NULL, '{item.email}'),
                    pec = IF('{item.pec}' = '', NULL, '{item.pec}'),
                    fax = IF('{item.fax}' = '', NULL, '{item.fax}')
                    WHERE id_cliente = '{id}'
                    """)
        MySql.close_connection_commit()

    @classmethod
    def create(cls, item : Client):
        MySql.open_connection()
        MySql.query(f"""
                    INSERT INTO cliente
                    (
                     id_cliente,
                     nome,
                     p_iva,
                     indirizzo,
                     cap,
                     iban,
                     telefono,
                     email,
                     pec,
                     fax)
                    VALUES
                    ('{item.id_cliente}',
                    IF('{item.nome}' = '', NULL, '{item.nome}'),
                    IF('{item.p_iva}' = '', NULL, '{item.p_iva}'),
                    IF('{item.indirizzo}' = '', NULL, '{item.indirizzo}'),
                    IF('{item.cap}' = '', NULL, '{item.cap}'),
                    IF('{item.iban}' = '', NULL, '{item.iban}'),
                    IF('{item.telefono}' = '', NULL, '{item.telefono}'),
                    IF('{item.email}' = '', NULL, '{item.email}'),
                    IF('{item.pec}' = '', NULL, '{item.pec}'),
                    IF('{item.fax}' = '', NULL, '{item.fax}'))
                    """)
        MySql.close_connection_commit()
