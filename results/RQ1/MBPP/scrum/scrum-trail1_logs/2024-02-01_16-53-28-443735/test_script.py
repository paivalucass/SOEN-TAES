def count_divisors(n):
    if n < 0:
        raise ValueError("Input integer cannot be negative")
    if n == 0:
        return False
    if n == 1:
        return False
    
    count = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            if n / i == i:
                count += 1
            else:
                count += 2
    
    return count % 2 == 0
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(count_divisors(10), True)

if __name__ == '__main__':
    unittest.main()