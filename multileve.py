class Animal:
    def speak(self):
        print("Animal Speaking")


class Dog (Animal):
    def bark(self):
        print("Vau VAu")


class childdog(Dog):
    def eat(self):
        print("Sab Khancha")

d=childdog()
d.speak()
d.bark()
d.eat()
    
