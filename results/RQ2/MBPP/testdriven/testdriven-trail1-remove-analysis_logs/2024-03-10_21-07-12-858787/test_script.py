def find_Rotations(str):
    n = len(str)
    for i in range(1, n+1):
        if n % i == 0:
            substring = str[:i]
            if substring * (n//i) == str:
                return i
    return n

assert find_Rotations("aaaa") == 1
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_Rotations('aaaa'), 1)

if __name__ == '__main__':
    unittest.main()