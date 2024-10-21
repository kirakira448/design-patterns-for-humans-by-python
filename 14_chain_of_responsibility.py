from abc import ABC, abstractmethod
from io import StringIO
import unittest
from unittest.mock import patch


class Account(ABC):
    def __init__(self, balance):
        self._successor = None
        self._balance = balance

    def set_next(self, account):
        self._successor = account

    def pay(self, amount_to_pay):
        if self.can_pay(amount_to_pay):
            print(f'Paid {amount_to_pay} using {self.__class__.__name__}')
        elif self._successor:
            print(f'Cannot pay using {self.__class__.__name__}. Proceeding ..')
            self._successor.pay(amount_to_pay)
        else:
            raise Exception('None of the accounts have enough balance')

    def can_pay(self, amount):
        return self._balance >= amount

class Bank(Account):
    def __init__(self, balance):
        super().__init__(balance)

class Paypal(Account):
    def __init__(self, balance):
        super().__init__(balance)

class Bitcoin(Account):
    def __init__(self, balance):
        super().__init__(balance)


class TestChainOfResponsibility(unittest.TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    def test_chain_of_responsibility(self, mock_stdout):
        """
        bank -> paypal -> bitcoin
        First priority bank
            if bank can't pay, then paypal
            if paypal can't pay, then bitcoin
        """
        bank = Bank(100)
        paypal = Paypal(200)
        bitcoin = Bitcoin(300)

        bank.set_next(paypal)
        paypal.set_next(bitcoin)
        bank.pay(259)
        self.assertEqual(mock_stdout.getvalue().strip(), "Cannot pay using Bank. Proceeding ..\nCannot pay using Paypal. Proceeding ..\nPaid 259 using Bitcoin")

if __name__ == "__main__":
    unittest.main()
