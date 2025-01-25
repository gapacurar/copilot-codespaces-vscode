import unittest
from CodingComments import Car

class TestCar(unittest.TestCase):
    def setUp(self):
        self.car1 = Car("Toyota", "Red", 180)
        self.car2 = Car("Honda", "Blue", 200)

    def test_get_name(self):
        self.assertEqual(self.car1.get_name(), "Toyota")
        self.assertEqual(self.car2.get_name(), "Honda")

    def test_get_color(self):
        self.assertEqual(self.car1.get_color(), "Red")
        self.assertEqual(self.car2.get_color(), "Blue")

    def test_get_max_speed(self):
        self.assertEqual(self.car1.get_max_speed(), 180)
        self.assertEqual(self.car2.get_max_speed(), 200)

    def test_str(self):
        self.assertEqual(str(self.car1), "Car(Name: Toyota, Color: Red, MaxSpeed: 180 km/h)")
        self.assertEqual(str(self.car2), "Car(Name: Honda, Color: Blue, MaxSpeed: 200 km/h)")

if __name__ == "__main__":
    unittest.main()