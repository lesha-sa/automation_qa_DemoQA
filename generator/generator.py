from faker.generator import random

from data.data import Person
from faker import Faker

faker_ru = Faker('ru_RU')
Faker.seed()

def generated_person():
    """
    Сreate random data for Person
    """
    yield Person(
       full_name = faker_ru.first_name() + " " + faker_ru.last_name() + " " + faker_ru.middle_name(),
        firstname = faker_ru.first_name(),
        lastname = faker_ru.last_name(),
        age = random.randint(10, 80),
        department = faker_ru.job(),
        salary = random.randint(10000, 80000),
        email = faker_ru.email(),
        current_address = faker_ru.address(),
        permanent_address = faker_ru.address(),
        mobile = faker_ru.msisdn(),
    )

def generated_file():
    """
    Create new file
    """
    path = rf'C:\proj\automation_qa_DemoQA\filetest{random.randint(0, 999)}.txt'
    file = open(path, 'w+')
    file.write(f'Hello world{random.randint(0, 999)}')
    file.close()
    return file.name, path


def generated_subject():
    all_subject = ["Hindi", "English", "Maths", "Physics","Chemistry", "Biology", "Computer Science",
    "Commerce", "Accounting", "Economics", "Arts", "Social Studies", "History", "Civics"]
    random_subject = random.randint(0, 13)
    return all_subject[random_subject]