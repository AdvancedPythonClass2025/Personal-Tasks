class Car:
    def __init__(self, model, year, color):
        self.model = model
        self.year = year
        self.color = color

    def display_info(self):
        print(f"model: {self.model}")
        print(f"year model: {self.year}")
        print(f"color: {self.color}")

    def change_color(self, new_color):
        self.color = new_color
        print(f"color of the car changed to: {new_color}")


my_car = Car("pride", 1399, "white")

my_car.display_info()

my_car.change_color("black")

my_car.display_info()
