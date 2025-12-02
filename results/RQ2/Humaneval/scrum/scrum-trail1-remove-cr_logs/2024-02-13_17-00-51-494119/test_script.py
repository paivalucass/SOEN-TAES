def digitSum(s):
    if not isinstance(s, str):
        return "Input should be a string"
    
    if not s:
        return 0
    
    sum_ascii = 0
    
    for char in s:
        if char.isupper():
            sum_ascii += ord(char)
    
    return sum_ascii
import unittest

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(digitSum(""), 0)
    
    def test2(self):
        self.assertEqual(digitSum("abAB"), 131)

    def test3(self):
        self.assertEqual(digitSum("abcCd"), 67)

    def test4(self):
        self.assertEqual(digitSum("helloE"), 69)

    def test5(self):
        self.assertEqual(digitSum("woArBld"), 131)

    def test6(self):
        self.assertEqual(digitSum("aAaaaXa"), 153)

if __name__ == '__main__':
    unittest.main()