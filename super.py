class Parent:
    def __init__(self,lastname,height,age,looks):
        self.lastname=lastname
        self.height=height
        self.age=age
        self.looks=looks
    
    def getlastname(self):
        return self.lastname

    def getheight(self):
        return self.height
    
    def getage(self):
        return self.age
    
    def getlooks(self):
        return self.looks
    

class Child (Parent):
    def __init__(self, lastname, height, age, looks,weight,firstname):
        super().__init__(lastname, height, age, looks)
        self.weight=weight
        self.firstname=firstname

    def getweight(self):
        return self.weight
    
    def getfirstname(self):
        return self.firstname

tekendra=Child("Rai","5",21,"Hot",65, "Tekendra")
print("lastname:", tekendra.getlastname())
print("height:", tekendra.getheight())
print("age:", tekendra.getage())
print("looks:", tekendra.getlooks())
print("weight:", tekendra.getweight())
print("firstname:", tekendra.getfirstname())






        