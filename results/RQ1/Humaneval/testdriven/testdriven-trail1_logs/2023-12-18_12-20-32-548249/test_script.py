from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any python values only for integers
    :param values: list of any python values
    :return: list of integers
    """
    if not isinstance(values, list):
        raise ValueError("Input must be a list of python values")

    result = [int(value) for value in values if isinstance(value, (int, float))]

    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(filter_integers(['a', 3.14, 5]), [5])
        self.assertEqual(filter_integers([1, 2, 3, 'abc', {}, []]), [1, 2, 3])

if __name__ == '__main__':
    unittest.main()