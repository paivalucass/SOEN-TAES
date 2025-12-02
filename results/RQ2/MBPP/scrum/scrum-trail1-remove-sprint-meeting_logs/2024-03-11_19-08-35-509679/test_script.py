def is_polite(n):
    count = 0
    num = 1
    while count < n:
        num += 1
        if is_polite_num(num):
            count += 1
    return num


def is_polite_num(num):
    factors = [1]
    for i in range(2, num//2 + 1):
        if num % i == 0:
            factors.append(i)
    return sum(factors) == num
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_polite(7), 11)

if __name__ == '__main__':
    unittest.main()