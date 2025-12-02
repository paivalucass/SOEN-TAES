def count_Occurrence(tup, lst):
    if not tup or not lst:
        raise ValueError("Input parameters cannot be empty")

    if not all(isinstance(item, (int, float, str)) for item in tup):
        raise TypeError("Tuple must contain only hashable elements")

    occurrence_count = {element: tup.count(element) for element in lst}

    return sum(occurrence_count.values())
import unittest

class Test(unittest.TestCase):
    
    def test_count_Occurrence(self):
        self.assertEqual(count_Occurrence(('a', 'a', 'c', 'b', 'd'),['a', 'b']), 3)

if __name__ == '__main__':
    unittest.main()