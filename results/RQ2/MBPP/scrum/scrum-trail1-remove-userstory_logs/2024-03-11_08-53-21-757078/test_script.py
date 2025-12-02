def divisor(n):
    count = 0
    if isinstance(n, int):
        if n > 0:
            for i in range(1, int(n**0.5) + 1):
                if n % i == 0:
                    if i * i == n:
                        count += 1
                    else:
                        count += 2
        return count
    else:
        return 0
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(divisor(15), 4)

if __name__ == '__main__':
    unittest.main()