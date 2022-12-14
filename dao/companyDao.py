from utils.db import MySql

class Company_dao:

    @classmethod
    def find_all(cls):
        MySql.openConnection()
        MySql.query("SELECT * FROM azienda")
        results = MySql.getResults()
        MySql.closeConnection()
        return results

    @classmethod
    def find_by_id(cls, id):
        MySql.openConnection()
        MySql.query(f"SELECT * FROM azienda WHERE id_azienda = {id}")
        results = MySql.getResults()
        MySql.closeConnection()
        return results

    @classmethod
    def remove_by_id(cls, id):
        MySql.openConnection()
        MySql.query(f"DELETE FROM azienda WHERE id_azienda = {id}")
        MySql.closeConnectionCommit()

    @classmethod
    def update_by_id(cls, key, value, id):
        MySql.openConnection()
        MySql.query(f"UPDATE azienda SET {key} = {value} WHERE id_azienda = {id}")
        MySql.closeConnectionCommit()

    @classmethod
    def insert_new(cls, item):
        MySql.openConnection()
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
                    ('{item['id_azienda']}',
                     '{item['nome']}',
                     '{item['p_iva']}',
                     '{item['indirizzo']}',
                     '{item['cap']}',
                     '{item['iban']}',
                     '{item['telefono']}',
                     '{item['email']}',
                     '{item['pec']}',
                     '{item['fax']}',)
                    """)
        MySql.closeConnectionCommit()
    