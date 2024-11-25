from request import Request


class TestCase:
    def __init__(self):
        self.request = Request()
        self.ID = str()
        self.response = str()

    def create_animal(self, name: str = 'Olaf') -> str:
        """
        Создание но вого животного через API-запрос.

        :param name: Имя животного, по умолчанию - Olaf
        :return: id созданного животного
        """
        data = {
                       "id": 0,
                       "category": {
                           "id": 0,
                           "name": "string"
                       },
                       "name": name,
                       "photoUrls": [
                           "string"
                       ],
                       "tags": [
                           {
                               "id": 0,
                               "name": "string"
                           }
                       ],
                       "status": "available"
                    }
        self.response = self.request.send_request('post', '/pet', data)
        self.ID = self.response.json()['id']
        return self.ID

    def find_animal(self, animal_id: str) -> dict:
        """
        Метод ищет животное по id.

        :param animal_id: id животного
        :return: информация о животном
        """
        url = f'/pet/{str(animal_id)}'
        self.response = self.request.send_request('get', url)
        return self.response.json()

    def remove_animal(self, animal_id: str) -> dict:
        """
        Метод удаляет животное по id.

        :param animal_id: id животного
        :return: request response в формате JSON
        """
        url = f'/pet/{str(animal_id)}'
        self.response = self.request.send_request('delete', url)
        return self.response.json()