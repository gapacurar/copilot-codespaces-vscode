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

if __name__ == "__main__":
    # Create two Car objects
    car1 = Car("Toyota", "Red", 150)
    car2 = Car("Honda", "Blue", 180)

    # Display their attributes
    print("Car 1:", car1)
    print("Car 2:", car2)