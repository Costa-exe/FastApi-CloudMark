from utils.db import MySql

class EmployeeCompanyDao:
    
    @classmethod
    def findAllEmployee_company(cls):
        MySql.openConnection()
        MySql.query("SELECT * FROM dipendente_azienda")
        results = MySql.getResults()
        MySql.closeConnection()
        return results

    @classmethod
    def findEmployeeId(cls, id_dipendente):
        MySql.openConnection()
        MySql.query(f"SELECT * FROM dipendente_azienda WHERE id_dipendente = '{id_dipendente}'")
        results = MySql.getResults()
        MySql.closeConnection()
        return results

    @classmethod
    def findCompanyId(cls, id_azienda):
        MySql.openConnection()
        MySql.query(f"SELECT * FROM dipendente_azienda WHERE id_azienda = '{id_azienda}'")
        results = MySql.getResults()
        MySql.closeConnection()
        return results

    @classmethod
    def removeByEmployeeId(cls, id_dipendente):
        MySql.openConnection()
        MySql.query(f"DELETE FROM dipendente_azienda WHERE id_dipendente = '{id_dipendente}'")
        MySql.closeConnectionCommit()

    @classmethod
    def removeByCompanyId(cls, id_azienda):
        MySql.openConnection()
        MySql.query(f"DELETE FROM dipendente_azienda WHERE id_azienda = '{id_azienda}'")
        MySql.closeConnectionCommit()

    @classmethod
    def updateByEmployeeId(cls, id_dipendente, item):
        MySql.openConnection()
        MySql.query(f"""
                    UPDATE dipendente_azienda
                    SET
                    id_dipendente = '{item['id_dipendente']}',
                    id_azienda = '{item['id_azienda']}',
                    data_inizio_rapporto = '{item['data_inizio_rapporto']}',
                    matricola = '{item['matricola']}',
                    data_fine_rapporto = '{item['data_fine_rapporto']}'
                    WHERE id_dipendente = '{id_dipendente}'
                    """)
        MySql.closeConnectionCommit()

    @classmethod
    def updateByCompanyId(cls, id_azienda, item):
        MySql.openConnection()
        MySql.query(f"""
                    UPDATE dipendente_azienda
                    SET
                    id_dipendente = '{item['id_dipendente']}',
                    id_azienda = '{item['id_azienda']}',
                    data_inizio_rapporto = '{item['data_inizio_rapporto']}',
                    matricola = '{item['matricola']}',
                    data_fine_rapporto = '{item['data_fine_rapporto']}'
                    WHERE id_azienda = '{id_azienda}'
                    """)
        MySql.closeConnectionCommit()        

    @classmethod
    def createNew(cls, item):
        MySql.openConnection()
        MySql.query(f"""
                    INSERT INTO dipendente_azienda
                    (
                     id_dipendente,
                     id_azienda,
                     data_inizio_rapporto,
                     matricola,
                     data_fine_rapporto
                    VALUES
                    ('{item['id_dipendente']}',
                     '{item['id_azienda']}',
                     '{item['data_inizio_rapporto']}',
                     '{item['matricola']}',
                     '{item['data_fine_rapporto']}')
                    """)
        MySql.closeConnectionCommit()
    


   
    