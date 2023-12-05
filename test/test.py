import unittest
from ..src.Insertion_Sort import insertion_sort

class TestInsertionSort(unittest.TestCase):
    def test_empty_list(self):
        arr = []
        insertion_sort(arr)
        self.assertEqual(arr, [])

    def test_single_element_list(self):
        arr = [1]
        insertion_sort(arr)
        self.assertEqual(arr, [1])

    def test_sorted_list(self):
        arr = [1, 2, 3, 4, 5]
        insertion_sort(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 5])

    def test_reverse_sorted_list(self):
        arr = [5, 4, 3, 2, 1]
        insertion_sort(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 5])

    def test_random_list(self):
        arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        insertion_sort(arr)
        self.assertEqual(arr, [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9])

if __name__ == '__main__':
    unittest.main()
