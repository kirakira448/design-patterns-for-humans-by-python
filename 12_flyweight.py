from abc import ABC, abstractmethod
import unittest

# Anything that will be cached is flyweight.
# Types of tea here will be flyweights.
class KarakTea:
    def __init__(self, flavor):
        self.flavor = flavor
    
    def __str__(self):
        return f"KarakTea with {self.flavor}"

class TeaMaker:
    def __init__(self):
        self.available_tea = {}

    def make(self, preference):
        self.available_tea[preference] = self.available_tea.get(preference, KarakTea(preference))
        return self.available_tea[preference]

class TeaShop:
    def __init__(self, tea_maker: TeaMaker):
        self.tea_maker = tea_maker
        self.orders = {}

    def take_order(self, tea_type, table):
        self.orders[table] = self.tea_maker.make(tea_type)

    def serve(self):
        for table, tea in self.orders.items():
            print(f"Serving tea to table {table}: {tea}")

class TestFlyweight(unittest.TestCase):
    def test_tea_shop(self):
        tea_maker = TeaMaker()
        tea_shop = TeaShop(tea_maker)
        tea_shop.take_order("less sugar", 1)
        tea_shop.take_order("more milk", 2)
        tea_shop.serve()

if __name__ == "__main__":
    unittest.main()

