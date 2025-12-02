def count_divisors(n):
    count = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            if i * i != n:
                count += 2
            else:
                count += 1
    if count % 2 == 0:
        return True
    else:
        return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(count_divisors(10), True)

if __name__ == '__main__':
    unittest.main()