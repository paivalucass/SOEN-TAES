def odd_Equivalent(s, n):
    count = 0
    for i in range(len(s)):
        if s[i] == '1':
            count += 1
    return min(count, n - count)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(odd_Equivalent("011001", 6), 3)

if __name__ == '__main__':
    unittest.main()