from abc import ABC, abstractmethod
import unittest


class Animal(ABC):
    @abstractmethod
    def accept(self, visitor: 'AnimalOperation'):
        pass

class AnimalOperation(ABC):
    @abstractmethod
    def visitMonkey(self, monkey: 'Monkey'):
        pass

    @abstractmethod
    def visitLion(self, lion: 'Lion'):
        pass

    @abstractmethod
    def visitDolphin(self, dolphin: 'Dolphin'):
        pass

class Monkey(Animal):
    def shout(self):
        print("Ooh ooh ooh!")

    def accept(self, visitor: AnimalOperation):
        visitor.visitMonkey(self)


class Lion(Animal):
    def roar(self):
        print("Roaaar!")

    def accept(self, visitor: AnimalOperation):
        visitor.visitLion(self)


class Dolphin(Animal):
    def speak(self):
        print("Tuut tuttu tuutt!")

    def accept(self, visitor: AnimalOperation):
        visitor.visitDolphin(self)


class Speak(AnimalOperation):
    def visitMonkey(self, monkey: Monkey):
        monkey.shout()

    def visitLion(self, lion: Lion):
        lion.roar()

    def visitDolphin(self, dolphin: Dolphin):
        dolphin.speak()


class Jump(AnimalOperation):
    def visitMonkey(self, monkey: Monkey):
        print("Jumped 20 feet high! on to the tree!")

    def visitLion(self, lion: Lion):
        print("Jumped 7 feet! Back on the ground!")

    def visitDolphin(self, dolphin: Dolphin):
        print("Walked on water a little and disappeared")

class TestVisitor(unittest.TestCase):
    def test_visitor(self):
        monkey = Monkey()
        lion = Lion()
        dolphin = Dolphin()
        speak = Speak()

        monkey.accept(speak)
        lion.accept(speak)
        dolphin.accept(speak)

        jump = Jump()
        monkey.accept(jump)
        lion.accept(jump)
        dolphin.accept(jump)

if __name__ == "__main__":
    unittest.main()
