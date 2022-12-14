from dao.clientDao import Client_dao
from models.clientModel import Client

class Client_dto:

    @classmethod
    def get_all(cls):
        clients = []
        results = Client_dao.find_all()
        for result in results:
                clients.append(Client(**result))
        return clients

    @classmethod
    def get_by_id(cls, id : str):
        result = Client_dao.find_by_id(id)
        return Client(**result[0])

    @classmethod
    def delete_by_id(cls, id : str):
        return Client_dao.remove_by_id(id)

    @classmethod
    def post(cls, item):
        return Client_dao.create_new(item)

    @classmethod
    def put(cls, id, item):
        return Client_dao.update_by_id(id, item)