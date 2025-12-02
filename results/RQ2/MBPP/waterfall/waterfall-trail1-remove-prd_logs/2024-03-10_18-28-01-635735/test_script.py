def divisor(n):
    if not isinstance(n, int):
        return "Error"
    
    count = 0
    for i in range(1, n+1):
        if n % i == 0:
            count += 1
    return count
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(divisor(15), 4)

if __name__ == '__main__':
    unittest.main()