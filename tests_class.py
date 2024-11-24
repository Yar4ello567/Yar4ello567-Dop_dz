from request import Request


class TestCase:
    def __init__(self):
        self.request = Request()
        self.ID = str()
        self.response = str()

    def create_animal(self, name: str = 'Olaf') -> str:
        """
        Создание нового животного через API-запрос
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
        self.response = self.request.send_request('post', 'pet', data)
        self.ID = self.response.json()['id']
        return self.ID

    def find_animal(self, animal_id: str) -> dict:
        """
        Метод ищет животное по id
        :param animal_id: id животного
        :return: информация о животном
        """
        url = 'pet/' + str(animal_id)
        self.response = self.request.send_request('get', url)
        return self.response.json()

    def delete_animal(self, animal_id: str) -> dict:
        """
        Метод удаляет животное по id через API-запрос
        :param animal_id: id животного
        :return: ответ сервера (статус удаления)
        """
        url = 'pet/' + str(animal_id)
        self.response = self.request.send_request('delete', url)
        return self.response.json()


class TestID:
    def __init__(self):
        self.test_case = TestCase()

    def check_deletion(self):
        """
        Проверка удаления животного по id:
        1. Создать животное с произвольным именем.
        2. Проверить, что животное существует.
        3. Удалить животное.
        4. Убедиться, что животное удалено (ожидаем ошибку при поиске).
        """
        created_id = self.test_case.create_animal(name='TestAnimal')

        animal_found = self.test_case.find_animal(animal_id=created_id)
        assert animal_found['id'] == created_id, "Ошибка: ID созданного животного не соответствует запросу."

        delete_response = self.test_case.delete_animal(animal_id=created_id)
        assert delete_response['message'] == str(created_id), "Ошибка: Животное не было удалено."

        try:
            self.test_case.find_animal(animal_id=created_id)
            assert False, "Ошибка: Животное по-прежнему существует."
        except Exception as exception:
            print(f"Животное с ID {created_id} успешно удалено. Ошибка при поиске: {str(exception)}")


# Пример использования
if __name__ == "__main__":
    test = TestID()
    test.check_deletion()
