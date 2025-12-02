def is_woodall(x):
    result = 1
    i = 1
    while result < x:
        i += 1
        result = i ** (i + 1)
    return result == x
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_woodall(383), True)

if __name__ == '__main__':
    unittest.main()