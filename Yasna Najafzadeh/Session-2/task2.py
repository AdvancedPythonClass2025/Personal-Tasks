class car :
    def __init__(self , model ,color , year):

        self.model = model
        self.color = color
        self.year = year

    def chang_color(self, new_color):
        
        self.color = new_color
    
    def display_info(self):

        print(
f'''
model: {self.model}
year:  {self.year}
color: {self.color}

''')


car1 = car("bmw" , "blue" ,"2001")

car1.chang_color("red")

car1.display_info()