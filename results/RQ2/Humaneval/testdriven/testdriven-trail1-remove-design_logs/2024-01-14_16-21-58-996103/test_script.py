def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..

    Args:
        lst: a non-empty list of integers

    Returns:
        int: the sum of even elements at odd indices
    """
    sum = 0
    if len(lst) == 0:
        return 0
    for i in range(1, len(lst), 2):
        if not isinstance(lst[i], int):
            return "Error: Invalid input"
        if lst[i] % 2 == 0:
            sum += lst[i]
    return sum
import unittest

class Test(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add([4, 2, 6, 7]), 2)

if __name__ == '__main__':
    unittest.main()