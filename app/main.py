class Person:
    people = {}

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age


def create_person_list(people: list) -> list:
    for p in people:
        person = Person(p["name"], p["age"])
        person.people[p["name"]] = person
    return person.__dict__