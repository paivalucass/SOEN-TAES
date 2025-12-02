def find_Rotations(str):
    n = len(str)
    for i in range(1, n+1):
        if n % i == 0 and str[:i] * (n // i) == str:
            return n // i
    return n
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_Rotations('aaaa'), 1)

if __name__ == '__main__':
    unittest.main()