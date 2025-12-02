def odd_Equivalent(s, n):
    s = s * 2
    count = 0
    for i in range(len(s)//2):
        if int(s[i:i+len(s)//2], 2) % 2 != 0:
            count += 1
    return count
import unittest

class Test(unittest.TestCase):
    def test_odd_equivalent(self):
        self.assertEqual(odd_Equivalent("011001", 6), 3)

if __name__ == '__main__':
    unittest.main()