from abc import ABC, abstractmethod
import unittest

class Door(ABC):
    @abstractmethod
    def open(self):
        pass

    @abstractmethod
    def close(self):
        pass

class LabDoor(Door):
    def open(self):
        print("Opening the lab door")

    def close(self):
        print("Closing the lab door")

class SecuredDoor(Door):
    def __init__(self, door: Door):
        self.door = door

    def open(self, password):
        if self.authenticate(password):
            self.door.open()
        else:
            print("Big no! It ain't possible.")

    def authenticate(self, password):
        return password == "$ecr3t"

    def close(self):
        self.door.close()

class TestProxy(unittest.TestCase):
    def test_proxy(self):
        door = SecuredDoor(LabDoor())
        door.open("invalid")
        door.open("$ecr3t")
        door.close()

if __name__ == "__main__":
    unittest.main()

