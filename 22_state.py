from abc import ABC, abstractmethod
import unittest


class PhoneState(ABC):
    @abstractmethod
    def pick_up(self):
        pass

    @abstractmethod
    def hang_up(self):
        pass

    @abstractmethod
    def dial(self):
        pass


class PhoneStateIdle(PhoneState):
    def pick_up(self):
        return PhoneStatePickedUp()

    def hang_up(self):
        raise Exception("Phone is already idle")

    def dial(self):
        raise Exception("unable to dial in idle state")


class PhoneStatePickedUp(PhoneState):
    def pick_up(self):
        raise Exception("Phone is already picked up")

    def hang_up(self):
        return PhoneStateIdle()

    def dial(self):
        return PhoneStateCalling()


class PhoneStateCalling(PhoneState):
    def pick_up(self):
        raise Exception("Phone is already picked up")

    def hang_up(self):
        return PhoneStateIdle()

    def dial(self):
        raise Exception("unable to dial in calling state")


class Phone:
    def __init__(self):
        self.state = PhoneStateIdle()

    def pick_up(self):
        self.state = self.state.pick_up()

    def hang_up(self):
        self.state = self.state.hang_up()

    def dial(self):
        self.state = self.state.dial()



class TestPhoneState(unittest.TestCase):
    def test_phone_state(self):
        phone = Phone()
        phone.pick_up()
        self.assertEqual(phone.state.__class__, PhoneStatePickedUp)
        phone.dial()
        self.assertEqual(phone.state.__class__, PhoneStateCalling)
        phone.hang_up()
        self.assertEqual(phone.state.__class__, PhoneStateIdle)


if __name__ == "__main__":
    unittest.main()

