class Plant :
    def __init__ (self,name,height,age):
        self.name =name
        self.height =height
        self.age =age
if __name__ == "__main__":
    p1 = Plant("Rose", 25, 30 )
    p2 = Plant("Sunflower", 80, 45)
    p3 = Plant("Cactus", 15, 120)
    garden =[p1,p2,p3]
for i in range (len(garden)):
    print(garden[i].name,":",garden[i].height,"cm",garden[i].age, "days old")
