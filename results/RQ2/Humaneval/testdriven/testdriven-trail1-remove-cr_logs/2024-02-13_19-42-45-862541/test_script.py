from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any python values only for integers

    Parameters:
    values (List[Any]): Input list containing python values

    Returns:
    List[int]: New list containing only the integer values from the input list
    """
    integer_values = [v for v in values if isinstance(v, int)]
    return integer_values

import unittest

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(filter_integers(['a', 3.14, 5]), [5])

    def test2(self):
        self.assertEqual(filter_integers([1, 2, 3, 'abc', {}, []]), [1, 2, 3])

if __name__ == '__main__':
    unittest.main()