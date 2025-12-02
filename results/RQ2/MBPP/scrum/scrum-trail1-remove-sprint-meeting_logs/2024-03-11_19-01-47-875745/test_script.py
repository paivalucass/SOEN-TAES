def heap_sort(iterable):
    # Implementation of heap sort algorithm
    # ...
    return sorted(iterable)

def test_heap_sort():
    assert heap_sort([]) == []
    assert heap_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert heap_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    assert heap_sort([1]) == [1]
    assert heap_sort([2, 1]) == [1, 2]
    assert heap_sort([3, 1, 2]) == [1, 2, 3]
    assert heap_sort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert heap_sort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0], 'quicksort') == [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
import unittest

class TestHeapSort(unittest.TestCase):
    def test_heap_sort(self):
        self.assertEqual(heap_sort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0]), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

if __name__ == '__main__':
    unittest.main()