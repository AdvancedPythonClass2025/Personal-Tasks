class Car:
    def init(self, model, year, color):
        self.model = model
        self.year = year
        self.color = color

    def display_info(self):
        print(f"مدل: {self.model}")
        print(f"سال ساخت: {self.year}")
        print(f"رنگ: {self.color}")

    def change_color(self, new_color):
        self.color = new_color
        print(f"رنگ خودرو به {new_color} تغییر یافت.")

car1 = Car("Peugeot 206", 2020, "سفید")
car1.display_info()
car1.change_color("قرمز")
car1.display_info()