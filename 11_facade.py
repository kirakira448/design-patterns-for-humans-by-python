from abc import ABC, abstractmethod
import unittest

class Computer:
    def get_electric_shock(self):
        return "Electric Shock"

    def make_sound(self):
        return "Beep Beep"

    def show_loading_screen(self):
        return "Loading..."
    
    def bam(self):
        return "Ready to be used!"
    
    def close_everything(self):
        return "Bup bup bup buzzzz"
    
    def sooth(self):
        return "Zzzzz"
    
    def pull_current(self):
        return "Haaah!"
    

class ComputerFacade:
    def __init__(self, computer: Computer):
        self.computer = computer

    def turn_on(self):
        return "\n".join([self.computer.get_electric_shock(), self.computer.make_sound(), self.computer.show_loading_screen(), self.computer.bam()])

    def turn_off(self):
        return "\n".join([self.computer.close_everything(), self.computer.sooth(), self.computer.pull_current()])

class TestFacade(unittest.TestCase):
    def test_computer_facade(self):
        computer = Computer()
        computer_facade = ComputerFacade(computer)
        self.assertEqual(computer_facade.turn_on(), "Electric Shock\nBeep Beep\nLoading...\nReady to be used!")
        self.assertEqual(computer_facade.turn_off(), "Bup bup bup buzzzz\nZzzzz\nHaaah!")

if __name__ == "__main__":
    unittest.main()


