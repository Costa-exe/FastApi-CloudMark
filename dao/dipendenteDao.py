from utils.db import MySql

class DipendenteDao:


    @classmethod
    def findAlldipendente(cls):
        MySql.openConnection()
        MySql.query("SELECT * FROM dipendente")
        results = MySql.getResults()
        MySql.closeConnection()
        return results

    
    @classmethod
    def findId_dipendente(cls):
        MySql.openConnection()
        MySql.query("SELECT id_dipendente FROM dipendente")
        results = MySql.getResults()
        MySql.closeConnection()
        return results


    @classmethod
    def findCf(cls):
        MySql.openConnection()
        MySql.query("SELECT cf FROM dipendente")
        results = MySql.getResults()
        MySql.closeConnection()
        return results

   
    @classmethod
    def findId_tipo_contratto(cls):
        MySql.openConnection()
        MySql.query("SELECT id_tipo_contratto FROM dipendente")
        results = MySql.getResults()
        MySql.closeConnection()
        return results

    