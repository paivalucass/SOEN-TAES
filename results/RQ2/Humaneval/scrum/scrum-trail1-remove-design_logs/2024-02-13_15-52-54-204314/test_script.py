def is_palindrome(string: str) -> bool:
    return string == string[::-1]

def make_palindrome(string: str) -> str:
    if len(string) == 0:
        return ""
    for i in range(len(string)):
        if string[i:] == string[i:][::-1]:
            return string + string[:i][::-1]
import unittest

class Test(unittest.TestCase):
    def test_is_palindrome(self):
        self.assertEqual(is_palindrome('madam'), True)
        self.assertEqual(is_palindrome('hello'), False)
    
    def test_make_palindrome(self):
        self.assertEqual(make_palindrome(''), '')
        self.assertEqual(make_palindrome('cat'), 'catac')
        self.assertEqual(make_palindrome('cata'), 'catac')

if __name__ == '__main__':
    unittest.main()