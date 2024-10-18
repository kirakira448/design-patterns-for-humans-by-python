from abc import ABC, abstractmethod
import unittest

class WebPage(ABC):

    @abstractmethod
    def display(self):
        pass

class About(WebPage):
    def __init__(self, theme: "Theme"):
        self.theme = theme

    def display(self):
        return f"Displaying About Page with {self.theme.get_color()} color"

class Careers(WebPage):
    def __init__(self, theme: "Theme"):
        self.theme = theme

    def display(self):
        return f"Displaying Careers Page with {self.theme.get_color()} color"

class Theme(ABC):
    @abstractmethod
    def get_color(self):
        pass
    
class DarkTheme(Theme):
    def get_color(self):
        return "Dark"

class LightTheme(Theme):
    def get_color(self):
        return "Light"
    
class AquaTheme(Theme):
    def get_color(self):
        return "Aqua"

class TestBridge(unittest.TestCase):
    def test_about_page_with_dark_theme(self):
        dark_theme = DarkTheme()
        about_page = About(dark_theme)
        self.assertEqual(about_page.display(), "Displaying About Page with Dark color")

    def test_careers_page_with_light_theme(self):
        light_theme = LightTheme()
        careers_page = Careers(light_theme)
        self.assertEqual(careers_page.display(), "Displaying Careers Page with Light color")

    def test_about_page_with_aqua_theme(self):
        aqua_theme = AquaTheme()    
        about_page = About(aqua_theme)
        self.assertEqual(about_page.display(), "Displaying About Page with Aqua color")

if __name__ == "__main__":
    unittest.main() 

