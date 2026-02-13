class Plant :
    def __init__ (self,name,height,age):
        self.name =name
        self.height =height
        self.age =age

    def get_info(self):
        print(f"Created: {self.name} ({self.height}cm, {self.age} days)")

if __name__ =="__main__":
    plants_data = [("Rose", 25, 30),
            ("Oak", 200, 365),
            ("Cactus", 5, 90),
            ("Sunflower", 80, 45),
            ("Fern", 15, 120)]
    print("=== Plant Factory Output ===")
    plants =[]
    for data in plants_data:
        plant = Plant (data[0],data[1],data[2])
        plants.append(plant)
        plant.get_info()
    print(f"\nTotal plants created: {len(plants)}")