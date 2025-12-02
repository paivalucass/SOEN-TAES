def odd_Equivalent(s, n):
    count = s.count('1')
    if n % 2 == 0:
        return min(count, len(s) - count)
    else:
        return max(count, len(s) - count)
import unittest

class Test(unittest.TestCase):
    def test_odd_Equivalent(self):
        self.assertEqual(odd_Equivalent("011001", 6), 3)

if __name__ == '__main__':
    unittest.main()