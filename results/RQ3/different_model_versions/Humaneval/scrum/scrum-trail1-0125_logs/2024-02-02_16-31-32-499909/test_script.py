def same_chars(s0: str, s1: str) -> bool:
    return sorted(s0) == sorted(s1)
import unittest

class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(same_chars('eabcdzzzz', 'dddzzzzzzzddeddabc'), True)
    
    def test_2(self):
        self.assertEqual(same_chars('abcd', 'dddddddabc'), True)
        
    def test_3(self):
        self.assertEqual(same_chars('dddddddabc', 'abcd'), True)
        
    def test_4(self):
        self.assertEqual(same_chars('eabcd', 'dddddddabc'), False)
        
    def test_5(self):
        self.assertEqual(same_chars('abcd', 'dddddddabce'), False)
        
    def test_6(self):
        self.assertEqual(same_chars('eabcdzzzz', 'dddzzzzzzzddddabc'), False)

if __name__ == '__main__':
    unittest.main()