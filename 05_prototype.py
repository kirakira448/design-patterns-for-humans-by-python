from abc import ABC, abstractmethod
import unittest
import copy

class Shape:
    def __init__(self):
        self._name = None
        self._category = None

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = value

    @property
    def category(self):
        return self._category
    
    @category.setter    
    def category(self, value):
        self._category = value
    
    def clone(self):
        return copy.deepcopy(self)

class TestShape(unittest.TestCase):
    def test_shape(self):
        shape = Shape()
        shape.name = "Jolly"
        shape.category = "Mountain Sheep"
        cloned_shape = shape.clone()
        cloned_shape.name = "Dolly"
        self.assertEqual(shape.name, "Jolly")
        self.assertEqual(shape.category, "Mountain Sheep")
        self.assertEqual(cloned_shape.name, "Dolly")
        self.assertEqual(cloned_shape.category, "Mountain Sheep")

if __name__ == "__main__":
    unittest.main()

        
