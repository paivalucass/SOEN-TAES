def is_polite(n):
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input must be a positive integer")

    def is_polite_number(num):
        divisors = set()
        for i in range(1, num):
            if num % i == 0:
                divisors.add(i)
        return sum(divisors) == num

    current_num = 1
    count = 0
    while True:
        if is_polite_number(current_num):
            count += 1
            if count == n:
                return current_num
        current_num += 1
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_polite(7), 11)

if __name__ == '__main__':
    unittest.main()