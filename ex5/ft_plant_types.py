class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name: str = name
        self.height: int = height
        self.age: int = age


class Flower(Plant):
    def __init__(
        self,
        name: str,
        height: int,
        age: int,
        color: str,
    ) -> None:
        super().__init__(name, height, age)
        self.color: str = color
        print(f"{name} (Flower): {height}cm, {age} days, {color} color")

    def bloom(self) -> None:
        print(f"{self.name} is blooming beautifully!")


class Tree(Plant):
    def __init__(
        self,
        name: str,
        height: int,
        age: int,
        trunk_diameter: int,
    ) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter: int = trunk_diameter
        print(
            f"{name} (Tree): {height}cm, "
            f"{age} days, {trunk_diameter}cm diameter"
        )

    def produce_shade(self, area: int) -> None:
        print(f"{self.name} provides {area} square meters of shade")


class Vegetable(Plant):
    def __init__(
        self,
        name: str,
        height: int,
        age: int,
        harvest_season: str,
        nutritional_value: str,
    ) -> None:
        super().__init__(name, height, age)
        self.harvest_season: str = harvest_season
        self.nutritional_value: str = nutritional_value
        print(
            f"{name} (Vegetable): {height}cm, "
            f"{age} days, {harvest_season} harvest"
        )
        print(f"{name} is rich in {nutritional_value}")


if __name__ == "__main__":
    print("=== Garden Plant Types ===\n")

    flower1 = Flower("Rose", 25, 30, "red")
    flower2 = Flower("Tulip", 20, 15, "yellow")
    flower1.bloom()
    flower2.bloom()

    print()

    tree1 = Tree("Oak", 500, 1825, 50)
    tree2 = Tree("Pine", 400, 1500, 40)
    tree1.produce_shade(78)
    tree2.produce_shade(60)

    print()

    vegetable1 = Vegetable("Tomato", 80, 90, "summer", "vitamin C")
    vegetable2 = Vegetable("Carrot", 30, 60, "spring", "vitamin A")
