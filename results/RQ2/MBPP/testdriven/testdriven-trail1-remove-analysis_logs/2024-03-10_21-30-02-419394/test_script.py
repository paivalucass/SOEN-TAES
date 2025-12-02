def count_divisors(n):
    '''
    This function counts the number of divisors for a given number and checks if the count is even.
    '''
    divisors_count = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            if i == n // i:
                divisors_count += 1
            else:
                divisors_count += 2
    return divisors_count % 2 == 0

assert count_divisors(10)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertTrue(count_divisors(10))

if __name__ == '__main__':
    unittest.main()