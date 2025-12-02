from typing import Tuple

def even_odd_count(num: int) -> Tuple[int, int]:
    even_count: int = 0
    odd_count: int = 0
    num_str: str = str(abs(num))
    for digit in num_str:
        if int(digit) % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return (even_count, odd_count)

import unittest

class Test(unittest.TestCase):
    def test_even_odd_count(self):
        self.assertEqual(even_odd_count(-12), (1, 1))
        self.assertEqual(even_odd_count(123), (1, 2))

if __name__ == '__main__':
    unittest.main()