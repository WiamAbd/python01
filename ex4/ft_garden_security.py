class SecurePlant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name: str = name
        self.__height: int = height
        self.__age: int = age
        print(f"Plant created: {name}")

    def set_height(self, value: int) -> None:
        if value < 0:
            print(
                f"Invalid operation attempted: "
                f"height {value}cm [REJECTED]"
            )
            print("Security: Negative height rejected")
        else:
            self.__height = value
            print(f"Height updated: {value}cm [OK]")

    def set_age(self, value: int) -> None:
        if value < 0:
            print(
                f"Invalid operation attempted: "
                f"age {value} days [REJECTED]"
            )
            print("Security: Negative age rejected")
        else:
            self.__age = value
            print(f"Age updated: {value} days [OK]")

    def get_height(self) -> int:
        return self.__height

    def get_age(self) -> int:
        return self.__age


if __name__ == "__main__":
    print("=== Garden Security System ===")

    plant = SecurePlant("Rose", 25, 30)

    plant.set_height(25)
    plant.set_age(30)
    plant.set_height(-5)

    print(
        f"Current plant: {plant.name} "
        f"({plant.get_height()}cm, {plant.get_age()} days)"
    )
