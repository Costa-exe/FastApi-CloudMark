from utils.db import MySql

class Contract_typeDao:
    
    @classmethod
    def findAll(cls):
        MySql.openConnection()
        MySql.query("SELECT * FROM tipo_contratto")
        results = MySql.getResults()
        MySql.closeConnection()
        return results

    @classmethod
    def findById(cls, id_tipo_contratto):
        MySql.openConnection()
        MySql.query(f"SELECT * FROM tipo_contratto WHERE id_tipo_contratto = '{id_tipo_contratto}'")
        results = MySql.getResults()
        MySql.closeConnection()
        return results

    @classmethod
    def findByName(cls, nome_tipo_contratto):
        MySql.openConnection()
        MySql.query(f"SELECT * FROM tipo_contratto WHERE nome_tipo_contratto = '{nome_tipo_contratto}'")
        results = MySql.getResults()
        MySql.closeConnection()
        return results

    @classmethod
    def removeById(cls, id_tipo_contratto):
        MySql.openConnection()
        MySql.query(f"DELETE FROM tipo_contratto WHERE id_tipo_contratto = '{id_tipo_contratto}'")
        MySql.closeConnectionCommit()

    @classmethod
    def removeByName(cls, nome_tipo_contratto):
        MySql.openConnection()
        MySql.query(f"DELETE FROM tipo_contratto WHERE nome_tipo_contratto = '{nome_tipo_contratto}'")
        MySql.closeConnectionCommit()

    @classmethod
    def updateById(cls, id_tipo_contratto, item):
        MySql.openConnection()
        MySql.query(f"""
                    UPDATE tipo_contratto
                    SET
                    id_tipo_contratto = '{item['id_tipo_contratto']}',
                    nome_tipo_contratto = '{item['nome_tipo_contratto']}',
                    descrizione = '{item['descrizione']}'
                    WHERE id_tipo_contratto = '{id_tipo_contratto}'
                    """)
        MySql.closeConnectionCommit()

    @classmethod
    def updateByName(cls, nome_tipo_contratto, item):
        MySql.openConnection()
        MySql.query(f"""
                    UPDATE tipo_contratto
                    SET
                    id_tipo_contratto = '{item['id_tipo_contratto']}',
                    nome_tipo_contratto = '{item['nome_tipo_contratto']}',
                    descrizione = '{item['descrizione']}'
                    WHERE id_tipo_contratto = '{nome_tipo_contratto}'
                    """)
        MySql.closeConnectionCommit()        

    @classmethod
    def createNew(cls, item):
        MySql.openConnection()
        MySql.query(f"""
                    INSERT INTO tipo_contratto
                    (
                     id_tipo_contratto,
                     nome_tipo_contratto,
                     descrizione
                    VALUES
                    ('{item['id_tipo_contratto']}',
                     '{item['nome_tipo_contratto']}',
                     '{item['descrizione']}')
                    """)
        MySql.closeConnectionCommit()
    


   