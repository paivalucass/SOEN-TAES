def odd_Equivalent(s, n):
    s = s[-n % len(s):] + s[:-n % len(s)]
    return sum([int(x) % 2 for x in s])
import unittest

class Test(unittest.TestCase):
    def test_odd_Equivalent(self):
        self.assertEqual(odd_Equivalent("011001", 6), 3)

if __name__ == '__main__':
    unittest.main()