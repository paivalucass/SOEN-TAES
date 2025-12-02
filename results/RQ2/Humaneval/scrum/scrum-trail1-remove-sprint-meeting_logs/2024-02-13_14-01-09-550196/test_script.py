def digitSum(s: str) -> int:
    if s is None or len(s) == 0:
        return 0
    
    sum_ascii = 0
    for char in s:
        if char.isupper():
            sum_ascii += ord(char)
    
    return sum_ascii
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