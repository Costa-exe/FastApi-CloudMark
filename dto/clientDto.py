from dao.clientDao import ClientDao
from models.clientModel import Client

class ClientDto:

    @classmethod
    def get_all(cls):
        clients = []
        results = ClientDao.find_all()
        for result in results:
                clients.append(Client(**result))
        return clients

    @classmethod
    def get_by_id(cls, id : str):
        result = ClientDao.find_by_id(id)
        return result

    @classmethod
    def delete(cls, id : str):
        return ClientDao.remove_by_id(id)

    @classmethod
    def post(cls, item : Client):
        return ClientDao.create(item)

    @classmethod
    def put(cls, id : str, item : Client):
        return ClientDao.update_by_id(id, item)