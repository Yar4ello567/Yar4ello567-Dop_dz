import pytest
from tests_class import TestCase


class TestID:

    @pytest.mark.parametrize("animal_name", ["Orlock", "Chinchilla"])
    def test_create_and_find_animal(self, animal_name):
        test = TestCase()
        animal_id = test.create_animal(animal_name)
        assert animal_id, "Не удалось создать животное!"

        animal = test.find_animal(animal_id)
        assert animal.get('id') == animal_id, f"Ожидалось ID {animal_id}, но получили {animal.get('id')}"  # Проверяем

    def test_remove_animal(self):
        test = TestCase()
        animal_id = test.create_animal("Chinchilla")
        assert animal_id, "Не удалось создать животное!"

        animal = test.find_animal(animal_id)
        assert animal.get('id') == animal_id, f"Ожидалось ID {animal_id}, но получили {animal.get('id')}"  # Проверяем

        test.remove_animal(animal_id)

        response = test.find_animal(animal_id)
        assert response.get('message') == "Pet not found", "Животное не было удалено!"
