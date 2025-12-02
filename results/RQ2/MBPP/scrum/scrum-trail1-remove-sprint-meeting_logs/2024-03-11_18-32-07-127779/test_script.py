def newman_prime(n):
    if n == 1:
        return 2
    elif n == 2:
        return 3
    else:
        count = 2
        num = 5
        while count < n:
            num += 2
            for i in range(3, int(num ** 0.5) + 1, 2):
                if num % i == 0:
                    break
            else:
                count += 1
        return num
import unittest

class Test(unittest.TestCase):
    def test_newman_prime(self):
        self.assertEqual(newman_prime(3), 7)

if __name__ == '__main__':
    unittest.main()