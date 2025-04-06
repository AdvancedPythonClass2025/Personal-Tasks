import os
def Clear():
    os.system("cls" if os.name == "nt" else "clear")
class Car :
    def __init__(self,model,rang,salsakht):
        self.model = model
        self.rang = rang
        self.salsakht = salsakht
    def namayesh_eteleat(self):
        print("model mashine : {} \n\nrang : {} \n\nsalsakht : {}\n".format(self.model,self.rang,self.salsakht))
    def taghir_rang(self,rang_jadid):
        self.rang = rang_jadid
        print('rang {} be ---{}--- taghire kard\n----------------------------'.format(self.model,rang_jadid))

car = Car("pride","sefid","1380")
car2 = Car("lamborgini","meshki","2023")
car3 = Car('partol',"gray","2000")
Clear()

car.namayesh_eteleat()
car.taghir_rang('ghermez')
car2.namayesh_eteleat()
car2.taghir_rang('abi')
car3.namayesh_eteleat()
car3.taghir_rang('meshki')
