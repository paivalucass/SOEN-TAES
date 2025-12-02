def opposite_Signs(x: int, y: int) -> bool:
    if not isinstance(x, int) or not isinstance(y, int):
        raise ValueError("Inputs should be integers")
    if x == 0 or y == 0:
        raise ValueError("Inputs cannot be zero")

    return (x < 0) != (y < 0)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(opposite_Signs(1, -2), True)

if __name__ == '__main__':
    unittest.main()