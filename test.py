class person:
   def __init__(self,name,age):
	   self.name=name
	   self.age=age
   def myfunc(self):
	   print("Hello my name is"+ self.name)
   def __str__(self):
	   return "Name:"+ self.name +",Age:"+ str(self.age)

p1 =person("John",36)
#p1.myfunc()
print(p1)