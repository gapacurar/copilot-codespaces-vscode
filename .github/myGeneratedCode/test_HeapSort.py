import unittest
from HeapSort import heap_sort

class TestHeapSort(unittest.TestCase):
    def test_sorted_array(self):
        arr = [12, 11, 13, 5, 6, 7]
        heap_sort(arr)
        self.assertEqual(arr, [5, 6, 7, 11, 12, 13])

    def test_reverse_sorted_array(self):
        arr = [5, 4, 3, 2, 1]
        heap_sort(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 5])

    def test_empty_array(self):
        arr = []
        heap_sort(arr)
        self.assertEqual(arr, [])

    def test_single_element_array(self):
        arr = [1]
        heap_sort(arr)
        self.assertEqual(arr, [1])

    def test_duplicate_elements_array(self):
        arr = [4, 1, 3, 2, 4, 1]
        heap_sort(arr)
        self.assertEqual(arr, [1, 1, 2, 3, 4, 4])

if __name__ == "__main__":
    unittest.main()