def swap_numbers(a, b):
    if isinstance(a, int) and isinstance(b, int):
        if a < 0 or b < 0:
            raise ValueError("Input should be positive integers")
        return (b, a)
    else:
        raise ValueError("Input should be integers")
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(swap_numbers(10, 20), (20, 10))

if __name__ == '__main__':
    unittest.main()