from request import Request


class TestCase:
    def __init__(self):
        self.request = Request()
        self.base_path = "http://petstore.swagger.io/v2"

    def create_animal(self, name: str = 'Olaf') -> str:
        payload = {
            "id": 0,
            "category": {"id": 0, "name": "string"},
            "name": name,
            "photoUrls": ["string"],
            "tags": [{"id": 0, "name": "string"}],
            "status": "available"
        }
        response = self.request.send_request('post', f'{self.base_path}pet', payload)
        if response.status_code not in (200, 201):
            raise ValueError(f"Ошибка создания: {response.status_code}. Ответ: {response.text}")

        animal_id = response.json().get('id')
        if not animal_id:
            raise KeyError(f"ID не найден в ответе: {response.json()}")
        return animal_id

    def find_animal(self, animal_id: str) -> dict:
        response = self.request.send_request('get', f'{self.base_path}pet/{animal_id}')
        if response.status_code == 404:
            return {"message": "Pet not found"}

        if response.status_code != 200:
            raise ValueError(f"Ошибка поиска: {response.status_code}. Ответ: {response.text}")

        return response.json()

    def remove_animal(self, animal_id: str) -> dict:
        response = self.request.send_request('delete', f'{self.base_path}pet/{animal_id}')
        if response.status_code != 200:
            raise ValueError(f"Ошибка удаления: {response.status_code}. Ответ: {response.text}")

        return response.json()
