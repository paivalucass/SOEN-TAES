def digitSum(s):
    total_sum = 0
    if isinstance(s, str):
        for char in s:
            if char.isupper():
                total_sum += ord(char)
    return total_sum
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(digitSum(''), 0)
        self.assertEqual(digitSum('abAB'), 131)
        self.assertEqual(digitSum('abcCd'), 67)
        self.assertEqual(digitSum('helloE'), 69)
        self.assertEqual(digitSum('woArBld'), 131)
        self.assertEqual(digitSum('aAaaaXa'), 153)

if __name__ == '__main__':
    unittest.main()