from abc import ABC, abstractmethod
import unittest


class SortStrategy(ABC):
    @abstractmethod
    def sort(self, dataset: list[int]):
        pass


class BubbleSortStrategy(SortStrategy):
    def sort(self, dataset: list[int]):
        print("Sorting using bubble sort")
        return dataset
    

class QuickSortStrategy(SortStrategy):
    def sort(self, dataset: list[int]):
        print("Sorting using quick sort")
        return dataset
    

class Sorter:
    def __init__(self, sorter_small: SortStrategy, sorter_big: SortStrategy):
        self.sorter_small = sorter_small
        self.sorter_big = sorter_big

    def sort(self, dataset: list[int]) -> list[int]:
        if len(dataset) > 5:
            return self.sorter_big.sort(dataset)
        else:
            return self.sorter_small.sort(dataset)


class TestStrategy(unittest.TestCase):
    def test_strategy(self):
        small_dataset = [1, 2, 3, 4, 5]
        big_dataset = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        sorter = Sorter(BubbleSortStrategy(), QuickSortStrategy())
        self.assertEqual(sorter.sort(small_dataset), [1, 2, 3, 4, 5])
        self.assertEqual(sorter.sort(big_dataset), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])


if __name__ == "__main__":
    unittest.main()
