def newman_prime(n):
    if n <= 0:
        return 'Invalid input'
    elif n == 1:
        return 2
    else:
        count = 1
        num = 2
        while count < n:
            num += 1
            if all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)):
                count += 1
        return num
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(newman_prime(3), 7)

if __name__ == '__main__':
    unittest.main()