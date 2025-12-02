def digitSum(s):
    sum_of_ascii = 0
    for char in s:
        if char.isupper():
            sum_of_ascii += ord(char)
    return sum_of_ascii
import unittest

class Test(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(digitSum(''), 0)

    def test_string_with_uppercase(self):
        self.assertEqual(digitSum('abAB'), 131)
        self.assertEqual(digitSum('abcCd'), 67)
        self.assertEqual(digitSum('helloE'), 69)
        self.assertEqual(digitSum('woArBld'), 131)
        self.assertEqual(digitSum('aAaaaXa'), 153)

if __name__ == '__main__':
    unittest.main()