from utils.db import MySql

class Client_dao:

    @classmethod
    def find_all(cls):
        MySql.openConnection()
        MySql.query("SELECT * FROM cliente")
        results = MySql.getResults()
        MySql.closeConnection()
        return results

    @classmethod
    def find_by_id(cls, id):
        MySql.openConnection()
        MySql.query(f"SELECT * FROM cliente WHERE id_cliente = '{id}'")
        results = MySql.getResults()
        MySql.closeConnection()
        return results

    @classmethod
    def remove_by_id(cls, id):
        MySql.openConnection()
        MySql.query(f"DELETE FROM cliente WHERE id_cliente = '{id}'")
        MySql.closeConnectionCommit()

    @classmethod
    def update_by_id(cls, id, item):
        MySql.openConnection()
        MySql.query(f"""
                    UPDATE cliente
                    SET
                    id_cliente = '{item['id_cliente']}',
                    nome = '{item['nome']}',
                    p_iva = '{item['p_iva']}',
                    indirizzo = '{item['indirizzo']}',
                    cap = '{item['cap']}',
                    iban = '{item['iban']}',
                    telefono = '{item['telefono']}',
                    email = '{item['email']}',
                    pec = '{item['pec']}',
                    fax = '{item['fax']}'
                    WHERE id_cliente = '{id}'
                    """)
        MySql.closeConnectionCommit()

    @classmethod
    def create_new(cls, item):
        MySql.openConnection()
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
                    ('{item['id_cliente']}',
                     '{item['nome']}',
                     '{item['p_iva']}',
                     '{item['indirizzo']}',
                     '{item['cap']}',
                     '{item['iban']}',
                     '{item['telefono']}',
                     '{item['email']}',
                     '{item['pec']}',
                     '{item['fax']}')
                    """)
        MySql.closeConnectionCommit()
