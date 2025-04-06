class Car :
    def __init__(self,model,rang,salsakht):
        self.model = model
        self.rang = rang
        self.salsakht = salsakht
    def namayesh_eteleat(self):
        print("model mashine : {} \nrang : {} \nsalsakht : {}".format(self.model,self.rang,self.salsakht))
car = Car("pride","sefid","1380")
car.namayesh_eteleat()