class Name:
    def __init__(self, name, hobby) -> None:
        if name not in ["Bohdan", "Anonymous", "Artem"]:
            raise ValueError("Invalid name")

        if not hobby:
            raise ValueError("Hobby must not be empty")

        self.name = name
        self.hobby = hobby


a = Name("Artem", "programming")
b = Name("Bodko", "football")
c = Name("Artem", "")
