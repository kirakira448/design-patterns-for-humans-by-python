from abc import ABC, abstractmethod
import unittest

class Burger:
    def __init__(self, builder: "BurgerBuilder"):
        self.size = builder.size
        self.cheese = builder.cheese
        self.lettuce = builder.lettuce
        self.tomato = builder.tomato
        self.onion = builder.onion
        self.pickle = builder.pickle

class BurgerBuilder:
    def __init__(self, size: str):
        self.size = size
        self.cheese = False
        self.lettuce = False
        self.tomato = False
        self.onion = False
        self.pickle = False

    def add_cheese(self):
        self.cheese = True

    def add_lettuce(self):
        self.lettuce = True

    def add_tomato(self):
        self.tomato = True

    def add_onion(self):
        self.onion = True

    def add_pickle(self):
        self.pickle = True

    def build(self) -> Burger:
        return Burger(self)

class TestBuilder(unittest.TestCase):
    def test_burger_builder(self):
        builder = BurgerBuilder("Large")
        builder.add_cheese()
        builder.add_lettuce()
        builder.add_tomato()
        builder.add_onion()
        builder.add_pickle()    
        burger = builder.build()
        self.assertEqual(burger.size, "Large")
        self.assertEqual(burger.cheese, True)
        self.assertEqual(burger.lettuce, True)
        self.assertEqual(burger.tomato, True)
        self.assertEqual(burger.onion, True)
        self.assertEqual(burger.pickle, True)

if __name__ == "__main__":
    unittest.main()
