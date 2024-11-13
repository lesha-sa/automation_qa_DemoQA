from dataclasses import dataclass


"""
create a dataclass to store randomly generated information about a person with the help of Faker"""

@dataclass
class Person:
    full_name: str = None
    email: str = None
    current_address: str = None
    permanent_address: str = None