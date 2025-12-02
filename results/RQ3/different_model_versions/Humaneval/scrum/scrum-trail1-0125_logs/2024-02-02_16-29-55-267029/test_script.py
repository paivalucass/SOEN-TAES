def even_odd_count(num):
    even = 0
    odd = 0
    num = abs(num)
    while num > 0:
        digit = num % 10
        if digit % 2 == 0:
            even += 1
        else:
            odd += 1
        num = num // 10
    return (even, odd)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(even_odd_count(-12), (1, 1))
        self.assertEqual(even_odd_count(123), (1, 2))

if __name__ == '__main__':
    unittest.main()