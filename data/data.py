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
    mobile: str = None


@dataclass()
class Color:
    color_name: list = None

@dataclass()
class Date:
    day: str = None
    month: str = None
    year: str = None
    time: str = None