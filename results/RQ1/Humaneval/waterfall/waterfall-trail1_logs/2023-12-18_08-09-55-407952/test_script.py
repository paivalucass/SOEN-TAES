from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    if not isinstance(values, list):
        raise ValueError("Input must be a list")
    
    integer_values = [value for value in values if isinstance(value, int)]
    return integer_values
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(filter_integers(['a', 3.14, 5]), [5])
        self.assertEqual(filter_integers([1, 2, 3, 'abc', {}, []]), [1, 2, 3])

if __name__ == '__main__':
    unittest.main()