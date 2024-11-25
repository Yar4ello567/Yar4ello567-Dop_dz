import requests
import json


class Request:
    def __init__(self, url='https://petstore.swagger.io/v2', path=''):
        self.url = url
        self.path = path
        self.headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json'
            }
        self.method = {
            'get': requests.get,
            'post': requests.post,
            'delete': requests.delete
            }
        self.data = 0
        self.response = 0

    def send_request(self, method: str, path: str, payload: dict = None):
        """
        Метод конструирует и отправляет HTTP-запрос.

        :param method: Метод запроса - POST, GET и т.д.
        :param path: URL запроса
        :param payload: Тело запроса
        :return: Полный ответ на запрос
        """
        full_url = self.url + path
        self.data = json.dumps(payload)
        params = {'url': full_url, 'headers': self.headers, 'data': self.data}
        self.response = self.method[method](**params)
        return self.response