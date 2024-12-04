from dataclasses import dataclass



@dataclass
class Person:
    """
    Сreate a dataclass to store randomly generated information about a person with the help of Faker
    """
    full_name: str = None
    firstname: str = None
    lastname: str = None
    age: int = None
    salary: int = None
    department: str = None
    email: str = None
    current_address: str = None
    permanent_address: str = None