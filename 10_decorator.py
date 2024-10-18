from abc import ABC, abstractmethod
import unittest

class Coffee(ABC):
    @abstractmethod
    def get_cost(self):
        pass

    @abstractmethod
    def get_description(self):
        pass

class SimpleCoffee(Coffee):
    def get_cost(self):
        return 10

    def get_description(self):
        return "Simple Coffee"

class MilkCoffee(Coffee):       
    def __init__(self, coffee: Coffee):
        self.coffee = coffee

    def get_cost(self):
        return self.coffee.get_cost() + 2

    def get_description(self):
        return self.coffee.get_description() + ", Milk"

class WhipCoffee(Coffee):
    def __init__(self, coffee: Coffee):
        self.coffee = coffee

    def get_cost(self):
        return self.coffee.get_cost() + 5
    
    def get_description(self):
        return self.coffee.get_description() + ", Whip"

class VanillaCoffee(Coffee):
    def __init__(self, coffee: Coffee):
        self.coffee = coffee

    def get_cost(self):
        return self.coffee.get_cost() + 3
    
    def get_description(self):
        return self.coffee.get_description() + ", Vanilla"

class TestDecorator(unittest.TestCase):
    def test_simple_coffee(self):
        coffee = SimpleCoffee()
        self.assertEqual(coffee.get_cost(), 10)
        self.assertEqual(coffee.get_description(), "Simple Coffee")

    def test_milk_coffee(self):
        coffee = MilkCoffee(SimpleCoffee())
        self.assertEqual(coffee.get_cost(), 12)
        self.assertEqual(coffee.get_description(), "Simple Coffee, Milk")

    def test_whip_coffee(self):
        coffee = WhipCoffee(SimpleCoffee())
        self.assertEqual(coffee.get_cost(), 15)
        self.assertEqual(coffee.get_description(), "Simple Coffee, Whip")

    def test_vanilla_coffee(self):
        coffee = VanillaCoffee(SimpleCoffee())
        self.assertEqual(coffee.get_cost(), 13)
        self.assertEqual(coffee.get_description(), "Simple Coffee, Vanilla")

    def test_milk_whip_coffee(self):
        someCoffee = SimpleCoffee()
        someCoffee = MilkCoffee(someCoffee)
        someCoffee = WhipCoffee(someCoffee)
        self.assertEqual(someCoffee.get_cost(), 17)
        self.assertEqual(someCoffee.get_description(), "Simple Coffee, Milk, Whip")

    def test_milk_whip_vanilla_coffee(self):
        someCoffee = SimpleCoffee()
        someCoffee = MilkCoffee(someCoffee)
        someCoffee = WhipCoffee(someCoffee)
        someCoffee = VanillaCoffee(someCoffee)
        self.assertEqual(someCoffee.get_cost(), 20)
        self.assertEqual(someCoffee.get_description(), "Simple Coffee, Milk, Whip, Vanilla")

if __name__ == "__main__":
    unittest.main() 


