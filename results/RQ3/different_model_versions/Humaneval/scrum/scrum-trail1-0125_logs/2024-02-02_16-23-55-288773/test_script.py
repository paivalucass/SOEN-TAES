def reverse_delete(s, c):
    s = ''.join([char for char in s if char not in c])
    return s, s == s[::-1]
import unittest

class Test(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(reverse_delete("abcde", "ae"), ('bcd', False))
    
    def test_case2(self):
        self.assertEqual(reverse_delete("abcdef", "b"), ('acdef', False))
    
    def test_case3(self):
        self.assertEqual(reverse_delete("abcdedcba", "ab"), ('cdedc', True))

if __name__ == '__main__':
    unittest.main()