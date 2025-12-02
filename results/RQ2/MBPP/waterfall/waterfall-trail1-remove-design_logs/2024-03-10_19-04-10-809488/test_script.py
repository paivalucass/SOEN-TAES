def opposite_signs(x, y):
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        raise ValueError("Input parameters must be valid and of the correct type")

    return (x < 0) != (y < 0)

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(opposite_Signs(1, -2), True)

if __name__ == '__main__':
    unittest.main()