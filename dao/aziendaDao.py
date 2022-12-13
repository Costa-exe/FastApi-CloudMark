from utils.db import MySql

class AziendaDao:

    @classmethod
    def findAllAziende(cls):
        MySql.openConnection()
        MySql.query("SELECT * FROM azienda")
        results = MySql.getResults()
        MySql.closeConnection()
        return results

    @classmethod
    def findAziendaById(cls, id):
        MySql.openConnection()
        MySql.query(f"SELECT * FROM azienda WHERE id_azienda = {id}")
        results = MySql.getResults()
        MySql.closeConnection()
        return results

    @classmethod
    def removeAziendaById(cls, id):
        MySql.openConnection()
        MySql.query(f"DELETE FROM azienda WHERE id_azienda = {id}")
        results = MySql.getResults()
        MySql.closeConnection()
        return results

    