class Plant:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def grow(self):
        self.height += 1
        print(f"{self.name} grew 1cm")

    def get_info(self):
        return f"{self.name}: {self.height}cm"


class FloweringPlant(Plant):
    def __init__(self, name, height, color):
        super().__init__(name, height)
        self.color = color
        self.blooming = True

    def get_info(self):
        status = "blooming" if self.blooming else "not blooming"
        return f"{self.name}: {self.height}cm, {self.color} flowers ({status})"


class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, color, prize_points):
        super().__init__(name, height, color)
        self.prize_points = prize_points

    def get_info(self):
        base = super().get_info()
        return f"{base}, Prize points: {self.prize_points}"


class Garden:
    def __init__(self, owner):
        self.owner = owner
        self.plants = []
        self.total_growth = 0

    def add_plant(self, plant):
        self.plants.append(plant)
        print(f"Added {plant.name} to {self.owner}'s garden")

    def grow_all(self):
        print(f"{self.owner} is helping all plants grow...")
        for plant in self.plants:
            plant.grow()
            self.total_growth += 1

    def generate_report(self):
        print(f"=== {self.owner}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.plants:
            print(f"- {plant.get_info()}")
        print(f"Plants added: {len(self.plants)}, Total growth: {self.total_growth}")


class GardenManager:
    total_gardens = 0  # class-level data

    def __init__(self):
        self.gardens = []
        GardenManager.total_gardens += 1

    def add_garden(self, garden):
        self.gardens.append(garden)

    def compare_scores(self):
        scores = {}
        for garden in self.gardens:
            score = sum(p.height for p in garden.plants)
            scores[garden.owner] = score
        return scores

    @classmethod
    def create_garden_network(cls):
        print("Creating garden network...")
        return cls()

    @staticmethod
    def validate_height(value):
        return value >= 0

    class GardenStats:
        @staticmethod
        def count_plant_types(garden):
            regular = 0
            flowering = 0
            prize = 0
            for plant in garden.plants:
                if isinstance(plant, PrizeFlower):
                    prize += 1
                elif isinstance(plant, FloweringPlant):
                    flowering += 1
                else:
                    regular += 1
            return regular, flowering, prize


if __name__ == "__main__":
    print("=== Garden Management System Demo ===")

    manager = GardenManager.create_garden_network()

    # Create gardens
    alice_garden = Garden("Alice")
    bob_garden = Garden("Bob")

    manager.add_garden(alice_garden)
    manager.add_garden(bob_garden)

    # Create plants
    oak = Plant("Oak Tree", 100)
    rose = FloweringPlant("Rose", 25, "red")
    sunflower = PrizeFlower("Sunflower", 50, "yellow", 10)

    # Add plants
    alice_garden.add_plant(oak)
    alice_garden.add_plant(rose)
    alice_garden.add_plant(sunflower)

    # Grow plants
    alice_garden.grow_all()

    # Generate report
    alice_garden.generate_report()

    # Statistics using nested class
    stats = GardenManager.GardenStats()
    regular, flowering, prize = stats.count_plant_types(alice_garden)
    print(f"Plant types: {regular} regular, {flowering} flowering, {prize} prize flowers")

    # Static method usage
    print("Height validation test:", GardenManager.validate_height(10))

    # Compare gardens
    scores = manager.compare_scores()
    print("Garden scores -", ", ".join(f"{k}: {v}" for k, v in scores.items()))

    print("Total gardens managed:", GardenManager.total_gardens)
