from dao.clientDao import Client_dao
from models.clientModel import Client

class Client_dto:

    @classmethod
    def get_all(cls):
        clients = []
        results = Client_dao.find_all()
        for result in results:
                clients.append(result)
        return clients

    @classmethod
    def get_by_id(cls, id : str):
        result = Client_dao.find_by_id(id)
        return result

    @classmethod
    def delete_by_id(cls, id : str):
        return Client_dao.remove_by_id(id)

    @classmethod
    def post(cls, item : Client):
        return Client_dao.create_new(item)

    @classmethod
    def put(cls, id : str, item : Client):
        return Client_dao.update_by_id(id, item)