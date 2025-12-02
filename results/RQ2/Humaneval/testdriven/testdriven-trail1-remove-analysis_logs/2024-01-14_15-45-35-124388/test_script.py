from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    return [value for value in values if isinstance(value, int)]
import unittest
from typing import List, Any

class Test(unittest.TestCase):
    def test_filter_integers(self):
        self.assertEqual(filter_integers(['a', 3.14, 5]), [5])
        self.assertEqual(filter_integers([1, 2, 3, 'abc', {}, []]), [1, 2, 3])

if __name__ == '__main__':
    unittest.main()