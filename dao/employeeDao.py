from utils.db import MySql

class EmployeeDao:


    @classmethod
    def findAllEmployee(cls):
        MySql.openConnection()
        MySql.query("SELECT * FROM dipendente")
        results = MySql.getResults()
        MySql.closeConnection()
        return results

    @classmethod
    def findById(cls, id_dipendente):
        MySql.openConnection()
        MySql.query(f"SELECT * FROM dipendente WHERE id_dipendente = '{id_dipendente}'")
        results = MySql.getResults()
        MySql.closeConnection()
        return results

    @classmethod
    def removeById(cls, id_dipendente):
        MySql.openConnection()
        MySql.query(f"DELETE FROM dipendente WHERE id_dipendente = '{id_dipendente}'")
        MySql.closeConnectionCommit()

    @classmethod
    def updateById(cls, id_dipendente, item):
        MySql.openConnection()
        MySql.query(f"""
                    UPDATE cliente
                    SET
                    id_dipendente = '{item['id_dipendente']}',
                    nome = '{item['nome']}',
                    cognome = '{item['cognome']}',
                    cf = '{item['cf']}',                   
                    iban = '{item['iban']}',
                    telefono = '{item['telefono']}',
                    email = '{item['email']}',
                    id_tipo_contratto = '{item['id_tipo_contratto']}',
                    fax = '{item['fax']}'
                    WHERE id_cliente = '{id_dipendente}'
                    """)
        MySql.closeConnectionCommit()

    @classmethod
    def createNew(cls, item):
        MySql.openConnection()
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
                    ('{item['id_cliente']}',
                     '{item['nome']}',
                     '{item['cognome']}',
                     '{item['cf']}',
                     '{item['iban']}',
                     '{item['telefono']}',
                     '{item['email']}',
                     '{item['id_tipo_contratto']}')
                    """)
        MySql.closeConnectionCommit()

    