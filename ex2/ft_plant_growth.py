class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name: str = name
        self.height: int = height
        self.age: int = age

    def grow(self) -> None:
        self.height += 6

    def age(self) -> None:
        self.age += 6

    def get_info(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")


if __name__ == "__main__":
    plant = Plant("Rose", 25, 30)

    initial_height: int = plant.height

    print("=== Day 1 ===")
    plant.get_info()

    plant.grow()
    plant.age()

    print("=== Day 7 ===")
    plant.get_info()

    final_height: int = plant.height
    growth: int = final_height - initial_height

    print(f"Growth this week: +{growth}cm")
