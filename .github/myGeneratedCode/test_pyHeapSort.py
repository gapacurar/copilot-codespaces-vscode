import unittest
from pyHeapSort import heap_sort

class TestHeapSort(unittest.TestCase):

    def test_heap_sort(self):
        arr = [3, 6, 8, 10, 1, 2, 1]
        heap_sort(arr)
        self.assertEqual(arr, [1, 1, 2, 3, 6, 8, 10])

    def test_heap_sort_empty(self):
        arr = []
        heap_sort(arr)
        self.assertEqual(arr, [])

    def test_heap_sort_single_element(self):
        arr = [1]
        heap_sort(arr)
        self.assertEqual(arr, [1])

    def test_heap_sort_sorted(self):
        arr = [1, 2, 3, 4, 5]
        heap_sort(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 5])

    def test_heap_sort_reverse_sorted(self):
        arr = [5, 4, 3, 2, 1]
        heap_sort(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 5])

if __name__ == "__main__":
    unittest.main(exit=False)