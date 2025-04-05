#ابتدا یک کلاس به اسم car ایجاد میکنیم 
#  Constructorکه کلید واژه  init بعد از  استفاده میکنیم 

class car:

    def __init__(self , model , color , year):
        self.model = model
        self.color = color
        self.year = year

    def display_info(self):
    
        print(f"model: {self.model}, year: {self.year}, color: {self.color}")
        
    def change_color(self, new_color):
        
        print(f"color changed to {self.color}")
    
        
        self.color = new_color
#نمایش اولیه اطلاعات خودرو
my_car = car("mercedes G_class ","black", 2025 )
my_car .display_info() 
#تغییر رنگ خودرو
my_car .change_color("dark red")
my_car .display_info()
