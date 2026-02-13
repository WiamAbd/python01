class Plant :
    def __init__ (self,name,height,age):
        self.name =name
        self.height =height
        self.age =age

    def grow(self):
        self.height += 6

    def aging(self):
        self.age += 6

    def get_info(self):
        print(f"{self.name}: {self.height}cm, {self.age} days old")





if __name__ =="__main__":
    pl = Plant("Rose", 25, 30)
    initialH = pl.height
    print("=== Day1===")
    pl.get_info()
    pl.grow()
    pl.aging()
    print("=== Day7===")
    pl.get_info()
    finalH = pl.height
    growth =finalH -initialH
    print(f"Growth this week: +{growth}cm")
