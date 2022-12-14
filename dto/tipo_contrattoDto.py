from dao.tipo_contrattoDao import Tipo_contrattoDao

class TipoContratto:
    def __init__(self, id_tipo_contratto, nome_tipo_contratto, descrizione = ""):
        self.id_tipo_contratto = id_tipo_contratto
        self.nome_tipo_contratto = nome_tipo_contratto
        self.descrizione = descrizione
       

class Tipo_contratto:
    @classmethod
    def getAlltipo_contratto(cls):
        data = Tipo_contrattoDao.findAlltipo_contratto()
        newList = []
        for lista in data:
            newList.append(TipoContratto(lista[0]))
        return newList


    @classmethod
    def getAllid_tipo_contratto(cls,id_tipo_contratto:int):
        data = Tipo_contrattoDao.findAlltipo_contratto()
        newList = []
        for lista in data:
            newList.append(id_tipo_contratto(lista[0]))
        return newList


        
    @classmethod
    def getAllnome_tipo_contratto(cls,nome_tipo_contratto):
        data = Tipo_contrattoDao.findAlltipo_contratto()
        newList = []
        for lista in data:
            newList.append(nome_tipo_contratto(lista[0]))
        return newList