class Vehicle:
    def __init__(self):
        self.vehicle_type = ""

    def get_user_input(self):
        self.vehicle_type = input("Enter vehicle type (car, truck, plane, boat, broomstick): ").lower()


class Automobile(Vehicle):
    def __init__(self):
        super().__init__()
        self.year = ""
        self.make = ""
        self.model = ""
        self.doors = ""
        self.roof = ""

    def get_user_input(self):
        super().get_user_input()
        self.year = input("Enter year: ")
        self.make = input("Enter make: ")
        self.model = input("Enter model: ")
        self.doors = input("Enter number of doors (2 or 4): ")
        self.roof = input("Enter type of roof (solid or sun roof): ")

    def display_vehicle_info(self):
        print("\nVehicle Information:")
        print("  Vehicle type:", self.vehicle_type)
        print("  Year:", self.year)
        print("  Make:", self.make)
        print("  Model:", self.model)
        print("  Number of doors:", self.doors)
        print("  Type of roof:", self.roof)


def main():
    automobile = Automobile()
    automobile.get_user_input()
    automobile.display_vehicle_info()


if __name__ == "__main__":
    main()
