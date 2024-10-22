from abc import ABC, abstractmethod
from datetime import datetime
import unittest


class ChatRoomMediator(ABC):
    @abstractmethod
    def show_message(self, user, message):
        pass

# Mediator
class ChatRoom(ChatRoomMediator):
    def show_message(self, user, message):
        time = datetime.now().strftime("%H:%M")
        sender = user.get_name()
        print(f"[{time}] {sender}: {message}")


class User:
    def __init__(self, name, chat_mediator):
        self.name = name
        self.chat_mediator = chat_mediator

    def get_name(self):
        return self.name
    
    def send(self, message):
        self.chat_mediator.show_message(self, message)


class TestMediator(unittest.TestCase):
    def test_mediator(self):
        mediator = ChatRoom()
        user1 = User("John", mediator)
        user2 = User("Jane", mediator)
        user1.send("Hi there!")
        user2.send("Hey!")
if __name__ == "__main__":
    unittest.main()
