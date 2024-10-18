from abc import ABC, abstractmethod
import unittest

class Door(ABC):
    @abstractmethod
    def get_description(self) -> str:
        pass

class WoodenDoor(Door):
    def get_description(self) -> str:
        return "I am a wooden door"

class IronDoor(Door):
    def get_description(self) -> str:
        return "I am an iron door"  

class DoorFittingExpert(ABC):
    @abstractmethod
    def get_description(self) -> str:
        pass

class Welder(DoorFittingExpert):
    def get_description(self) -> str:
        return "I can only fit iron doors"

class Carpenter(DoorFittingExpert):
    def get_description(self) -> str:
        return "I can only fit wooden doors"

class DoorFactory(ABC):
    @abstractmethod
    def make_door(self) -> Door:
        pass

    @abstractmethod
    def make_fitting_expert(self) -> DoorFittingExpert:
        pass

class WoodenDoorFactory(DoorFactory):
    """
    Wooden factory to return carpenter and wooden door
    """
    def make_door(self) -> Door:
        return WoodenDoor()

    def make_fitting_expert(self) -> DoorFittingExpert:
        return Carpenter()

class IronDoorFactory(DoorFactory):
    """
    Iron factory to return welder and iron door
    """

    def make_door(self) -> Door:
        return IronDoor()

    def make_fitting_expert(self) -> DoorFittingExpert:
        return Welder()


class TestAbstractFactory(unittest.TestCase):
    def test_wooden_door_factory(self):
        wooden_door_factory = WoodenDoorFactory()
        self.assertEqual(wooden_door_factory.make_door().get_description(), "I am a wooden door")
        self.assertEqual(wooden_door_factory.make_fitting_expert().get_description(), "I can only fit wooden doors")

    def test_iron_door_factory(self):
        iron_door_factory = IronDoorFactory()   
        self.assertEqual(iron_door_factory.make_door().get_description(), "I am an iron door")
        self.assertEqual(iron_door_factory.make_fitting_expert().get_description(), "I can only fit iron doors")

if __name__ == "__main__":
    unittest.main()
