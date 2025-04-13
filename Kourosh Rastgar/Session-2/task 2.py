class Car:
    def __init__(self, model, year, color):
        self.model = model
        self.year = year
        self.color = color

    def display_info(self):
        print(f"مدل: {self.model}")
        print(f"سال ساخت: {self.year}")
        print(f"رنگ: {self.color}")

    def change_color(self, new_color):
        self.color = new_color
        print(f"رنگ خودرو به {new_color} تغییر کرد.")


my_car = Car("پراید", 1399, "سفید")

my_car.display_info()

my_car.change_color("مشکی")

my_car.display_info()