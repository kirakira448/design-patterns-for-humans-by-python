from abc import ABC, abstractmethod
import unittest

class Door(ABC):
    """
    Abstract class for a door.
    """
    @abstractmethod
    def get_width(self) -> float:
        pass

    @abstractmethod
    def get_height(self) -> float:
        pass

class DoorFactory:
    """
    Factory class for creating doors.
    """
    @staticmethod
    def make_door(width: float, height: float) -> 'Door':
        return WoodenDoor(width, height)

class WoodenDoor(Door):
    """
    Concrete class for a wooden door.
    """
    def __init__(self, width: float, height: float):
        self._width = width
        self._height = height

    def get_width(self) -> float:
        return self._width

    def get_height(self) -> float:
        return self._height

class TestWoodenDoor(unittest.TestCase):
    """
    Test class for the WoodenDoor class.
    """
    def test_get_width(self):
        door = WoodenDoor(10, 20)
        self.assertEqual(door.get_width(), 10)

    def test_get_height(self):
        door = WoodenDoor(10, 20)
        self.assertEqual(door.get_height(), 20)

class TestDoorFactory(unittest.TestCase):
    """
    Test class for the DoorFactory class.
    """
    def test_make_door(self):
        door = DoorFactory.make_door(10, 20)
        self.assertEqual(door.get_width(), 10)
        self.assertEqual(door.get_height(), 20)

if __name__ == "__main__":
    unittest.main()
