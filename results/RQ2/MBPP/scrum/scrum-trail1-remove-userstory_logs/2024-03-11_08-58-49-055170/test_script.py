def min_of_three(a: int, b: int, c: int) -> int:
    try:
        if type(a) not in (int, float) or type(b) not in (int, float) or type(c) not in (int, float):
            raise ValueError("Input parameters must be valid numbers")
        return min(a, b, c)
    except TypeError:
        raise ValueError("Input parameters must be valid numbers")
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(min_of_three(10, 20, 0), 0)

if __name__ == '__main__':
    unittest.main()