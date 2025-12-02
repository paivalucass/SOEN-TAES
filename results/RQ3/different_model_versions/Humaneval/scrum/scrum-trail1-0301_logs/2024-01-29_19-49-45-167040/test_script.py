from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """ Filter given list of any python values only for integers
    >>> filter_integers(['a', 3.14, 5])
    [5]
    >>> filter_integers([1, 2, 3, 'abc', {}, []])
    [1, 2, 3]
    """
    integer_list = []
    for value in values:
        if isinstance(value, int):
            integer_list.append(value)
        elif isinstance(value, str) and value.isdigit():
            integer_list.append(int(value))
    return integer_list
import unittest
from typing import List, Any

class Test(unittest.TestCase):
    def test_filter_integers(self):
        self.assertEqual(filter_integers(['a', 3.14, 5]), [5])
        self.assertEqual(filter_integers([1, 2, 3, 'abc', {}, []]), [1, 2, 3])
        self.assertEqual(filter_integers([1, 'hello', 2.2, -4, [5, 6]]), [1, -4])

if __name__ == '__main__':
    unittest.main()