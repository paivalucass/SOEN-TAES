def is_perfect_square(n):
    try:
        if n < 0:
            return False
        sqrt_n = n ** 0.5
        return sqrt_n.is_integer()
    except (TypeError, ValueError):
        return "Error"

assert not is_perfect_square(10)
assert is_perfect_square(9)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_perfect_square(10), False)

if __name__ == '__main__':
    unittest.main()