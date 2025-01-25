class Car:
    """
    The Car class represents a car with a name, color, and maximum speed.

    Attributes:
        name (str): The name of the car.
        color (str): The color of the car.
        max_speed (int): The maximum speed of the car in km/h.
    """
    def __init__(self, name, color, max_speed):
        """
        Initializes the Car object with the given name, color, and maximum speed.

        Args:
            name (str): The name of the car.
            color (str): The color of the car.
            max_speed (int): The maximum speed of the car in km/h.
        """
        self.name = name
        self.color = color
        self.max_speed = max_speed

    def __str__(self):
        """
        Returns a string representation of the Car object.

        Returns:
            str: A string describing the car.
        """
        return f"Car(Name: {self.name}, Color: {self.color}, MaxSpeed: {self.max_speed} km/h)"

    def get_name(self):
        """
        Returns the name of the car.

        Returns:
            str: The name of the car.
        """
        return self.name

    def get_color(self):
        """
        Returns the color of the car.

        Returns:
            str: The color of the car.
        """
        return self.color

    def get_max_speed(self):
        """
        Returns the maximum speed of the car.

        Returns:
            int: The maximum speed of the car in km/h.
        """
        return self.max_speed

def bubble_sort_cars(cars):
    n = len(cars)
    for i in range(n):
        for j in range(0, n-i-1):
            if cars[j].get_max_speed() > cars[j+1].get_max_speed():
                cars[j], cars[j+1] = cars[j+1], cars[j]

if __name__ == "__main__":
    # Create 10 Car objects
    cars = [
        Car("Toyota", "Red", 180),
        Car("Honda", "Blue", 200),
        Car("Ford", "Green", 160),
        Car("Chevrolet", "Yellow", 190),
        Car("BMW", "Black", 220),
        Car("Audi", "White", 210),
        Car("Mercedes", "Silver", 230),
        Car("Volkswagen", "Purple", 170),
        Car("Nissan", "Orange", 150),
        Car("Hyundai", "Pink", 140)
    ]

    # Display original list of cars
    print("Original list of cars:")
    for car in cars:
        print(car)

    # Sort the cars based on their maximum speed using bubble sort
    bubble_sort_cars(cars)

    # Display sorted list of cars
    print("\nSorted list of cars by max speed:")
    for car in cars:
        print(car)
