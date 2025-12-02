def is_Diff(n):
    return n % 11 == 0

# Rewrite your code here to pass all the test cases.
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_Diff(12345), False)

if __name__ == '__main__':
    unittest.main()