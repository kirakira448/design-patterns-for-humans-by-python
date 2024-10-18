from abc import ABC, abstractmethod
import unittest

class Lion(ABC):
    @abstractmethod
    def roar(self):
        pass


class AfricanLion(Lion):
    def roar(self):
        return "African Lion Roar"

class AsianLion(Lion):
    def roar(self):
        return "Asian Lion Roar"
        

class Hunter:
    def hunt(self, lion: Lion):
        return lion.roar()

# This needs to be added to the game
class WildDog:
    def bark(self):
        return "Wild Dog Bark"

# This needs to be added to the game
class WildDogAdapter(Lion):
    def __init__(self, wild_dog: WildDog):
        self.wild_dog = wild_dog

    def roar(self):
        return self.wild_dog.bark()


class TestAdapter(unittest.TestCase):
    def test_wild_dog_adapter(self):
        wild_dog = WildDog()
        wild_dog_adapter = WildDogAdapter(wild_dog)

        hunter = Hunter()
        self.assertEqual(hunter.hunt(wild_dog_adapter), "Wild Dog Bark")

if __name__ == "__main__":
    unittest.main()









