from utils.db import MySql
from models.companyModel import Company


class CompanyDao:

    @classmethod
    def find_all(cls):
        MySql.open_connection()
        MySql.query("SELECT * FROM azienda")
        results = MySql.get_results()
        MySql.close_connection()
        return results

    @classmethod
    def find_id_by_name(cls, name: str):
        MySql.open_connection()
        MySql.query(f"SELECT id_azienda FROM azienda WHERE nome = '{name}'")
        result = MySql.get_result()
        MySql.close_connection()
        return result

    @classmethod
    def find_by_id(cls, id: str):
        MySql.open_connection()
        MySql.query(f"SELECT * FROM azienda WHERE id_azienda = '{id}'")
        results = MySql.get_result()
        MySql.close_connection()
        return results

    @classmethod
    def remove_by_id(cls, id: str):
        MySql.open_connection()
        MySql.query(f"DELETE FROM azienda WHERE id_azienda = '{id}'")
        MySql.close_connection_commit()

    @classmethod
    def update_by_id(cls, id: str, item: Company):
        MySql.open_connection()
        MySql.query(f"""
                    UPDATE azienda
                    SET
                    id_azienda = '{item.id_azienda}',
                    nome = IF('{item.nome}' = 'None', NULL,'{item.nome}'),
                    p_iva = IF('{item.p_iva}' = 'None', NULL, '{item.p_iva}'),
                    indirizzo = IF('{item.indirizzo}' = 'None', NULL, '{item.indirizzo}'),
                    cap = IF('{item.cap}' = 'None', NULL, '{item.cap}'),
                    iban = IF('{item.iban}' = 'None', NULL, '{item.iban}'),
                    telefono = IF('{item.telefono}' = 'None', NULL, '{item.telefono}'),
                    email = IF('{item.email}' = 'None', NULL, '{item.email}'),
                    pec = IF('{item.pec}' = 'None', NULL, '{item.pec}'),
                    fax = IF('{item.fax}' = 'None', NULL, '{item.fax}')
                    WHERE id_azienda = '{id}'
                    """)
        MySql.close_connection_commit()

    @classmethod
    def create(cls, item: Company):
        MySql.open_connection()
        MySql.query(f"""
                    INSERT INTO azienda
                    (
                     id_azienda,
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
                    ('{item.id_azienda}',
                    IF('{item.nome}' = 'None', NULL, '{item.nome}'),
                    IF('{item.p_iva}' = 'None', NULL, '{item.p_iva}'),
                    IF('{item.indirizzo}' = 'None', NULL, '{item.indirizzo}'),
                    IF('{item.cap}' = 'None', NULL, '{item.cap}'),
                    IF('{item.iban}' = 'None', NULL, '{item.iban}'),
                    IF('{item.telefono}' = 'None', NULL, '{item.telefono}'),
                    IF('{item.email}' = 'None', NULL, '{item.email}'),
                    IF('{item.pec}' = 'None', NULL, '{item.pec}'),
                    IF('{item.fax}' = 'None', NULL, '{item.fax}'))
                    """)
        MySql.close_connection_commit()
