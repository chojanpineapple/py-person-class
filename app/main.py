class Person:
    people = {}

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.people[name] = Person


def create_person_list(people: list) -> list:
    result = [
    (
        {**p, "wife": p.get("wife") or next(
            (x["name"] for x in people if x.get("husband") == p["name"]),
            None
        )}
        if "wife" in p
        else
        {**p, "husband": p.get("husband") or next(
            (x["name"] for x in people if x.get("wife") == p["name"]),
            None
        )}
    )
    for p in people
]

    for p in people:
        person = Person(p["name"], p["age"])
    return result