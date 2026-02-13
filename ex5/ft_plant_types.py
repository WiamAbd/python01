class Plant :
    def __init__ (self,name,height,age):
        self.name =name
        self.height =height
        self.age =age

class Flower(Plant):
    def __init__ (self,name,height,age,color):
        super().__init__(name, height, age)
        self.color =color
        print(f"{name} (Flower): {height}cm, {age} days, {color} color")
    
    def bloom(self):
        print("Rose is blooming beautifully!")
class Tree(Plant):
    def __init__ (self,name,height,age,trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter=trunk_diameter
        print(f"{name} (Tree): {height}cm, {age} days, {trunk_diameter}cm diameter")
    def produce_shade(self,x):
        print(f"{self.name} provides {x} square meters of shade")
class Vegetable(Plant): 
    def __init__ (self,name,height,age,harvest_season,nutritional_value): 
        super().__init__(name, height, age)
        self.harvest_season=harvest_season
        self.nutritional_value=nutritional_value
        print(f"{name} (Vegetable): {height}cm, {age} days, {harvest_season} harvest")
        print(name,"is rich in",nutritional_value)

if __name__=="__main__":
    print("=== Garden Plant Types ===\n")
    flower1 =Flower("Rose",25,30,"red")
    flower1.bloom()
    print("\n")
    tree1 =Tree("Oak",500,1825,50)
    tree1.produce_shade(78)
    print("\n")
    vege =Vegetable("Tomato",80,90,"summer"," vitamin C")