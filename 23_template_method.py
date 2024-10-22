from abc import ABC, abstractmethod
import unittest


class Builder(ABC):
    def build(self):
        self.test()
        self.lint()
        self.assemble()
        self.deploy()

    @abstractmethod
    def test(self):
        pass

    @abstractmethod
    def lint(self):
        pass

    @abstractmethod
    def assemble(self):
        pass

    @abstractmethod
    def deploy(self):
        pass


class AndroidBuilder(Builder):
    def test(self):
        print("Running android tests")

    def lint(self):
        print("Linting android code")

    def assemble(self):
        print("Assembling android code")

    def deploy(self):
        print("Deploying android code")


class IosBuilder(Builder):
    def test(self):
        print("Running ios tests")

    def lint(self):
        print("Linting ios code")

    def assemble(self):
        print("Assembling ios code")

    def deploy(self):
        print("Deploying ios code")


class TestBuilder(unittest.TestCase):
    def test_android_builder(self):
        builder = AndroidBuilder()
        builder.build()

    def test_ios_builder(self):
        builder = IosBuilder()
        builder.build()



if __name__ == "__main__":
    unittest.main()
