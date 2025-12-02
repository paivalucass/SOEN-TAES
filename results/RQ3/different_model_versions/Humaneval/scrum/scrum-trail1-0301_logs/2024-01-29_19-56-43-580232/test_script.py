def digitSum(s):
    class NotUppercaseError(Exception):
        pass
        
    try:
        if not isinstance(s, str):
            raise TypeError("Input should be a string.")
        
        result = 0
        
        for ch in s:
            if ch.isupper():
                result += ord(ch)
                
        return result
    
    except NotUppercaseError:
        raise NotUppercaseError("Input should contain at least one uppercase letter.")
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