class Car:
    def __init__(self, color, model):  # اینجا باید __init__ باشه
        self.color = color
        self.model = model

    def my_info(self):
        print(f"My car: {self.color}, model: {self.model}")

mycar = Car("yellow", "pejoct")
mycar.my_info()
