import os
def Clear():
    os.system("cls" if os.name == "nt" else "clear")
class Car :
    def __init__(self,model,rang,salsakht):
        self.model = model
        self.rang = rang
        self.salsakht = salsakht
    def namayesh_eteleat(self):
        print("model mashine : {} \nrang : {} \nsalsakht : {}".format(self.model,self.rang,self.salsakht))
Clear()
car = Car("pride","sefid","1380")
car.namayesh_eteleat()
