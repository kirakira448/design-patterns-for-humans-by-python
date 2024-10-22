from abc import ABC, abstractmethod
from io import StringIO
import unittest
from unittest.mock import patch

# Receiver
class Bulb:
    def turn_on(self):
        print("Bulb has been lit")

    def turn_off(self):
        print("Darkness!")

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass

    @abstractmethod
    def redo(self):
        pass


class TurnOn(Command):
    def __init__(self, bulb):
        self.bulb = bulb

    def execute(self):
        self.bulb.turn_on()

    def undo(self):
        self.bulb.turn_off()

    def redo(self):
        self.execute()

class TurnOff(Command):
    def __init__(self, bulb):
        self.bulb = bulb

    def execute(self):
        self.bulb.turn_off()

    def undo(self):
        self.bulb.turn_on()

    def redo(self):
        self.execute()


# Invoker
class RemoteControl:
    def submit(self, command):
        command.execute()


class TestCommand(unittest.TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    def test_command(self, mock_stdout):
        bulb = Bulb()
        turn_on = TurnOn(bulb)
        turn_off = TurnOff(bulb)

        remote = RemoteControl()

        remote.submit(turn_on)
        remote.submit(turn_off)

        self.assertEqual(mock_stdout.getvalue().strip(), "Bulb has been lit\nDarkness!")

if __name__ == "__main__":
    unittest.main()
