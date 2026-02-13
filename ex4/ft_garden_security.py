class SecurePlant:
    def __init__(self,name,height,age):
        self.name =name
        self.__height =height
        self.__age =age
        print("Plant created:",name)
    def set_height(self,x):
        if (x<0):
            print(f"Invalid operation attempted: height {x}cm  [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self.__height =x
            print(f"Height updated: {x}cm [OK]")
    def set_age(self,x):
        if (x<0):
            print(f"Invalid operation attempted: age {x} days  [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self.__age =x
            print(f"Age updated: {x} days [OK]")
    def get_height(self):
        return self.__height
    def get_age(self):
        return self.__age
    
if __name__ =="__main__":
    print("=== Garden Security System ===")
    plant = SecurePlant("Rose",25,30)
    plant.set_height(25)
    plant.set_age(30)
    plant.set_height(-5)
    print(f"\nCurrent plant: {plant.name} ({plant.get_height()}cm, {plant.get_age()} days)")

