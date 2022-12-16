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
    def find_by_id(cls, id : str):
        MySql.open_connection()
        MySql.query(f"SELECT * FROM azienda WHERE id_azienda = '{id}'")
        results = MySql.get_result()
        MySql.close_connection()
        return results

    @classmethod
    def remove_by_id(cls, id : str):
        MySql.open_connection()
        MySql.query(f"DELETE FROM azienda WHERE id_azienda = '{id}'")
        MySql.close_connectionCommit()

    @classmethod
    def update_by_id(cls, id : str, item : Company):
        MySql.open_connection()
        MySql.query(f"""
                    UPDATE azienda
                    SET
                    id_azienda = '{item.id_azienda}',
                    nome = '{item.nome}',
                    p_iva = '{item.p_iva}',
                    indirizzo = '{item.indirizzo}',
                    cap = '{item.cap}',
                    iban = '{item.iban}',
                    telefono = '{item.telefono}',
                    email = '{item.email}',
                    pec = '{item.pec}',
                    fax = '{item.fax}'
                    WHERE id_azienda = '{id}'
                    """)
        MySql.close_connectionCommit()

    @classmethod
    def create(cls, item : Company):
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
                     '{item.nome}',
                     '{item.p_iva}',
                     '{item.indirizzo}',
                     '{item.cap}',
                     '{item.iban}',
                     '{item.telefono}',
                     '{item.email}',
                     '{item.pec}',
                     '{item.fax}')
                    """)
        MySql.close_connectionCommit()
    