class car:
    def __init__(self,name,model,colour):
        self.name=name
        self.model=model
        self.colour=colour
    def myfunc(self):
        print(f"Name of the car is {self.name} ,model {self.model} and colour {self.colour}")
    def __str__(self):
        return "Car name:"+ self.name + ",model:"+ self.model + ",colour:" + self.colour
    def __add__(self, other):
        return self.name + other.name
    
p1= car("Audi","Q3","red")
p2= car("oodi","Q3","red")
p1.myfunc()
print(p1)
print(p1+p2)