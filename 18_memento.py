from abc import ABC, abstractmethod
import unittest


class EditorMemento:
    def __init__(self, content):
        self.content = content

    def get_content(self):
        return self.content


class Editor:
    def __init__(self):
        self.content = ""

    def type(self, words):
        self.content += " " + words

    def get_content(self):
        return self.content.strip()

    def save(self):
        return EditorMemento(self.content)

    def restore(self, memento):
        self.content = memento.get_content()


class TestMemento(unittest.TestCase):
    def test_memento(self):
        editor = Editor()
        editor.type("This is a line of text.")
        memento = editor.save()
        editor.type("This is another line of text.")
        self.assertEqual(editor.get_content(), "This is a line of text. This is another line of text.")
        editor.restore(memento)
        self.assertEqual(editor.get_content(), "This is a line of text.")

if __name__ == "__main__":
    unittest.main()

