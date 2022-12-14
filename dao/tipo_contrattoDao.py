from utils.db import MySql

class Tipo_contrattoDao:
    
    @classmethod
    def findAlltipo_contratto(cls):
        MySql.openConnection()
        MySql.query("SELECT * FROM tipo_contratto")
        results = MySql.getResults()
        MySql.closeConnection()
        return results

    @classmethod
    def findId_tipo_contratto(cls):
        MySql.openConnection()
        MySql.query("SELECT id_tipo_contratto FROM tipo_contratto")
        results = MySql.getResults()
        MySql.closeConnection()
        return results

    @classmethod
    def findNome_tipo_contratto(cls):
        MySql.openConnection()
        MySql.query("SELECT nome_tipo_contratto FROM tipo_contratto")
        results = MySql.getResults()
        MySql.closeConnection()
        return results

    

   