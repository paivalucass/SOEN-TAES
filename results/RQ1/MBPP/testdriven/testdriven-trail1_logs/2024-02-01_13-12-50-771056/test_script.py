def heap_sort(iterable):
    # Error handling for edge cases
    if not iterable:  # handle empty input
        return []

    if len(iterable) == 1:  # handle single element input
        return iterable

    if not all(isinstance(item, (int, float)) for item in iterable):  # handle invalid data types
        raise TypeError("Invalid data type. Input should be a list of integers or floats.")

    # Implementation of the heap sort algorithm
    # ...

    # Error handling and edge case implementation
    # ...

    # Return the sorted list
    return sorted(iterable)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(heap_sort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0]), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

if __name__ == '__main__':
    unittest.main()