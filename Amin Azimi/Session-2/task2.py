def init(self, model, year, color):
        self.model = model
        self.year = year
        self.color = color

    def display_info(self):
        print(f"Model: {self.model}, Year: {self.year}, Color: {self.color}")

    def change_color(self, new_color):
        self.color = new_color
        print(f"The color has been changed to {self.color}")
