class Plant:
    def __init__(self, name: str, height: int) -> None:
        self.name: str = name
        self.height: int = height
        self.growth: int = 0

    def show_infos(self) -> None:
        print(f"- {self.name}: {self.height}cm")

    def grow_plant(self) -> None:
        self.height += 1
        self.growth += 1

    def get_type(self) -> str:
        return "regular"


class FloweringPlant(Plant):
    def __init__(
        self,
        name: str,
        height: int,
        color: str,
    ) -> None:
        super().__init__(name, height)
        self.color: str = color
        self.blooming: bool = True

    def show_infos(self) -> None:
        print(
            f"- {self.name}: {self.height}cm, "
            f"{self.color} flowers (blooming)"
        )

    def get_type(self) -> str:
        return "flowering"


class PrizeFlower(FloweringPlant):
    def __init__(
        self,
        name: str,
        height: int,
        color: str,
        prize_points: int,
    ) -> None:
        super().__init__(name, height, color)
        self.prize_points: int = prize_points

    def show_infos(self) -> None:
        print(
            f"- {self.name}: {self.height}cm, "
            f"{self.color} flowers (blooming), "
            f"Prize points: {self.prize_points}"
        )

    def get_type(self) -> str:
        return "prize"


class Garden:
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.plants: list[Plant] = []

    def add_plant(self, plant: Plant) -> None:
        self.plants.append(plant)
        print(f"Added {plant.name} to {self.name}'s garden")

    def grow_all(self) -> None:
        print(f"{self.name} is helping all plants grow...")
        for plant in self.plants:
            plant.grow_plant()
            print(f"{plant.name} grew 1cm")

    def garden_report(self) -> None:
        print(f"=== {self.name}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.plants:
            plant.show_infos()


class GardenManager:
    def __init__(self) -> None:
        self.gardens: list[Garden] = []

    @classmethod
    def create_garden_network(cls) -> "GardenManager":
        print("Creating garden network...")
        return cls()

    def add_garden(self, garden: Garden) -> None:
        self.gardens.append(garden)

    @staticmethod
    def validate_height(value: int) -> bool:
        return value >= 0

    def compare_scores(self) -> None:
        results: list[str] = []

        for garden in self.gardens:
            total_height: int = 0
            for plant in garden.plants:
                total_height += plant.height
            results.append(f"{garden.name}: {total_height}")

        print("Garden scores - " + ", ".join(results))
        print(f"Total gardens managed: {len(self.gardens)}")

    class GardenStats:
        @staticmethod
        def calculate_analytics(
            gardens: list["Garden"],
        ) -> None:
            total_plants: int = 0
            total_growth: int = 0
            regular: int = 0
            flowering: int = 0
            prize: int = 0

            for garden in gardens:
                for plant in garden.plants:
                    total_plants += 1
                    total_growth += plant.growth

                    plant_type: str = plant.get_type()

                    if plant_type == "prize":
                        prize += 1
                    elif plant_type == "flowering":
                        flowering += 1
                    else:
                        regular += 1

            print(
                f"Plants added: {total_plants}, "
                f"Total growth: {total_growth}cm"
            )
            print(
                f"Plant types: {regular} regular, "
                f"{flowering} flowering, "
                f"{prize} prize flowers"
            )


if __name__ == "__main__":
    print("=== Garden Management System Demo ===")

    manager: GardenManager = (
        GardenManager.create_garden_network()
    )

    alice_garden: Garden = Garden("Alice")
    bob_garden: Garden = Garden("Bob")

    manager.add_garden(alice_garden)
    manager.add_garden(bob_garden)

    oak: Plant = Plant("Oak Tree", 100)
    rose: FloweringPlant = FloweringPlant("Rose", 25, "red")
    sunflower: PrizeFlower = PrizeFlower(
        "Sunflower",
        50,
        "yellow",
        10,
    )

    cactus: Plant = Plant("Cactus", 40)
    tulip: FloweringPlant = FloweringPlant(
        "Tulip",
        20,
        "pink",
    )

    alice_garden.add_plant(oak)
    alice_garden.add_plant(rose)
    alice_garden.add_plant(sunflower)

    alice_garden.grow_all()

    alice_garden.garden_report()

    GardenManager.GardenStats.calculate_analytics(
        manager.gardens
    )

    manager.compare_scores()
