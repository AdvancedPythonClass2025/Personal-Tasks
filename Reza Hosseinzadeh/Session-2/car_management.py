
def CClear():
    import os
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

class mashin:
    def __init__(self , model ,sal_tolid , rang, vazn ):

        self.model = model
        self.sal_tolid = sal_tolid
        self.rang = rang
        self.vazn = vazn

    def etelaat(self):

        print(f"\n{self.model} |  sale sakht: {self.sal_tolid} | rang: {self.rang} | vazn: {self.vazn}\n")
    
    def spray(self , rang_jadid):
        rang_gadim = self.rang
        self.rang = rang_jadid
        print(f"rang az '{rang_gadim}' be '{self.rang}' taghir kard")

car1 = mashin("Pride" , 1398 , "nok-medadi" , "600Kg")
car2 = mashin("L90" , 1384 , "sefid" , "870Kg")
car3 = mashin("samand" , 1392 , "meshki" , "950Kg")
car4 = mashin("peykan" , 1365 , "ghermes" , "720Kg")

CClear()
car3.etelaat()
car3.spray("sefid")
car3.etelaat()