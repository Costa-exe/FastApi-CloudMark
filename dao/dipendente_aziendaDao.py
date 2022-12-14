from utils.db import MySql

class DipendenteAziendaDao:
    
    @classmethod
    def findAlldipendente_azienda(cls):
        MySql.openConnection()
        MySql.query("SELECT * FROM dipendente_azienda")
        results = MySql.getResults()
        MySql.closeConnection()
        return results


    @classmethod
    def findId_dipendente(cls):
        MySql.openConnection()
        MySql.query("SELECT id_dipendente FROM dipendente_azienda")
        results = MySql.getResults()
        MySql.closeConnection()
        return results

    @classmethod
    def findId_azienda(cls):
        MySql.openConnection()
        MySql.query("SELECT id_azienda FROM dipendente_azienda")
        results = MySql.getResults()
        MySql.closeConnection()
        return results


    @classmethod
    def findMatricola(cls):
        MySql.openConnection()
        MySql.query("SELECT matricola FROM dipendente_azienda")
        results = MySql.getResults()
        MySql.closeConnection()
        return results


    