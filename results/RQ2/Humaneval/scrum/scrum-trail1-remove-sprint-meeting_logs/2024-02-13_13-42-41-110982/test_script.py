from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    if not isinstance(values, list):
        raise ValueError("Input is not a list")

    return [x for x in values if isinstance(x, int)]
import unittest

class Test(unittest.TestCase):
    def test_filter_integers(self):
        self.assertEqual(filter_integers(['a', 3.14, 5]), [5])
        self.assertEqual(filter_integers([1, 2, 3, 'abc', {}, []]), [1, 2, 3])

if __name__ == '__main__':
    unittest.main()