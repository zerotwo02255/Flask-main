class jeff:
    
    age=12
    type ="shark"
    def __init__(self,name,age):
        print("obj created")
        self.type=name
        print(name,age)
        
    def __str__(self):
       return f"{self.age}"
        
        
        
    def kale(self,a,b):
        print(self.type)
        return a+a+b
    
     
    def lol(self):
        print("chak ko dulo")
    

obj1=jeff("raand",30)
print(obj1)
x=obj1.kale(1,2)