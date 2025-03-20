#ابتدا یک کلاس ایجاد میکنیم 
#  Constructorکه کلید واژه  init بعد از  استفاده میکنیم 

class car:

    def __init__(self , model , color , year):
        self.model = model
        self.color = color
        self.year = year
        