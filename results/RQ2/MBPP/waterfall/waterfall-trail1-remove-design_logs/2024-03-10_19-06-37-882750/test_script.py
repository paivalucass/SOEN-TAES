def odd_equivalent(s: str, n: int) -> int:
    count = 0
    for i in range(len(s)):
        temp = s[-1] + s[:-1]
        count += temp.count('1')
        s = temp
    return count
import unittest

class Test(unittest.TestCase):
    def test_odd_Equivalent(self):
        self.assertEqual(odd_Equivalent("011001", 6), 3)

if __name__ == '__main__':
    unittest.main()