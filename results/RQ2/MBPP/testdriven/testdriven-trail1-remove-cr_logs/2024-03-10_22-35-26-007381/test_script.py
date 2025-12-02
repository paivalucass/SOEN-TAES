from typing import Tuple

def swap_numbers(a: float, b: float) -> Tuple[float, float]:
    try:
        result = (b, a)
        return result
    except ValueError:
        print("Invalid input. Please enter numeric values for a and b.")

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(swap_numbers(10, 20), (20, 10))

if __name__ == '__main__':
    unittest.main()