class  Car:
    def __init__(self, model, color, year, for_sale):
        self.model=model
        self.color=color
        self.year=year
        self.color=color
        self.for_sale=for_sale

    def drive(self):
        print(f"Drive the Car {self.color} {self.model}")

    def stop(self):
        print(f"Stop the Car {self.color} {self.model}")

    def describ(self):
        print(f"{self.model} {self.year} {self.color}")
