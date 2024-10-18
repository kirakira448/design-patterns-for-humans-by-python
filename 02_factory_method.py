from abc import ABC, abstractmethod
import unittest


class Interviewer(ABC):
    """
    Abstract class for an interviewer.
    """
    @abstractmethod
    def ask_questions(self):
        pass

class Developer(Interviewer):
    """
    Concrete class for a developer.
    """
    def ask_questions(self):
        print("Asking about design patterns!")
        
class CommunityExecutive(Interviewer):
    """
    Concrete class for a community executive.
    """
    def ask_questions(self):
        print("Asking about community building!")

class HiringManager(ABC):
    """
    Abstract class for a hiring manager.
    """
    # Factory method
    @abstractmethod
    def make_interviewer(self) -> Interviewer:
        pass

    def take_interview(self):
        """
        Method for taking an interview.
        """
        interviewer = self.make_interviewer()
        interviewer.ask_questions()

class DevelopmentManager(HiringManager):
    """
    Concrete class for a development manager.
    """
    def make_interviewer(self) -> Interviewer:
        return Developer()

class MarketingManager(HiringManager):
    """
    Concrete class for a marketing manager.
    """
    def make_interviewer(self) -> Interviewer:
        return CommunityExecutive()

class TestFactoryMethod(unittest.TestCase):
    """
    Test class for the factory method.
    """
    def test_development_manager(self):
        manager = DevelopmentManager()
        manager.take_interview()

    def test_marketing_manager(self):
        manager = MarketingManager()
        manager.take_interview()

if __name__ == "__main__":
    unittest.main()
        
        
