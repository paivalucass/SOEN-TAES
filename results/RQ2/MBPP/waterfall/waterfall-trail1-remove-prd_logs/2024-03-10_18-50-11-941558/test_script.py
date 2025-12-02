def test_three_equal(x: int, y: int, z: int) -> int:
    if not all(isinstance(i, int) for i in [x, y, z]):
        raise ValueError("All parameters must be integers")
    
    if x == y == z:
        return 3
    elif x == y or x == z or y == z:
        return 2
    else:
        return 0
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(test_three_equal(1, 1, 1), 3)

if __name__ == '__main__':
    unittest.main()