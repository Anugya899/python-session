class Prabhat:
    def assignment(self):
        print("I am doing assignment")

class Tekendra(Prabhat):
    def assignment(self):
        super().assignment()
        print("sab ko same cha kina sareko")

t=Tekendra()
t.assignment()
