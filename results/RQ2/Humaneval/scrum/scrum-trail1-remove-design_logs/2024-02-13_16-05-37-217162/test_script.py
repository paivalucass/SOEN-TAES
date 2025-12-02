def add(x: int, y: int) -> int:
    if not isinstance(x, int) or not isinstance(y, int):
        raise TypeError("Inputs must be integers")
    return x + y

# Unit tests
def test_add():
    assert add(2, 3) == 5
    assert add(5, 7) == 12
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    assert add(1000000, 1) == 1000001
    assert add(-1000000, -1) == -1000001

import unittest

class Test(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(5, 7), 12)

if __name__ == '__main__':
    unittest.main()