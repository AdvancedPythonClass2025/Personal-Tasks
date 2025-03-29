class car :
    def __init__(self  ,color ,brand, year):

        self.color = color
        self.brand = brand
        self.year = year

    def change_color(self, new_color):
        self.color = new_color
    
    def display_info(self):
        print(f'\n{self.brand}: {self.color} , {self.year}\n')


v1 = car( "black" ,"cheverlet","1987")
v1.display_info()
v1.change_color("brown")
v1.display_info()