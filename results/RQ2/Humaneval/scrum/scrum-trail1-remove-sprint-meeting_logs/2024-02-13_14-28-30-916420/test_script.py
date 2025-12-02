from typing import Tuple

def even_odd_count(num: int) -> Tuple[int, int]:
    even_count = 0
    odd_count = 0
    num = abs(num)
    while num > 0:
        digit = num % 10
        if digit % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
        num = num // 10
    return (even_count, odd_count)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(even_odd_count(-12), (1, 1))
        self.assertEqual(even_odd_count(123), (1, 2))

if __name__ == '__main__':
    unittest.main()