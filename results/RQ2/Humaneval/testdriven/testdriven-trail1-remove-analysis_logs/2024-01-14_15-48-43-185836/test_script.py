def add(x: int, y: int) -> int:
    """
    Add two numbers x and y
    :param x: int
    :param y: int
    :return: int, sum of x and y
    """
    if not isinstance(x, int) or not isinstance(y, int):
        raise ValueError("Invalid Input. x and y must be integers.")

    return x + y

# Test cases
assert add(2, 3) == 5
assert add(5, 7) == 12
assert add(-2, 3) == 1
assert add(0, 0) == 0
assert add(2147483647, 1) == 2147483648
assert add(-2147483648, -1) == -2147483649
import unittest

class Test(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(5, 7), 12)

if __name__ == '__main__':
    unittest.main()