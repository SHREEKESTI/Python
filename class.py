class Car:
    def __init__(self, brand, num, year):
        self.brand = brand
        self.num = num
        self.year = year

    def display_info(self):
        print(f"{self.brand} {self.num} ({self.year})")

    def start_engine(self):
        print("Engine started.")

car1=Car("BMW",4567,2024)
car1.display_info()
car1.start_engine()