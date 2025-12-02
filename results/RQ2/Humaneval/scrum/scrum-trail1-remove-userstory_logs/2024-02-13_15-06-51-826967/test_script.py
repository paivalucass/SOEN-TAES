def is_palindrome(text: str):
    if len(text) <= 1:
        return True
    
    text = ''.join(e for e in text if e.isalnum()).lower()
    
    left, right = 0, len(text) - 1
    while left < right:
        if text[left] != text[right]:
            return False
        left += 1
        right -= 1
    return True
import unittest

class Test(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(is_palindrome(''), True)

    def test_palindrome_string(self):
        self.assertEqual(is_palindrome('aba'), True)
        self.assertEqual(is_palindrome('aaaaa'), True)

    def test_non_palindrome_string(self):
        self.assertEqual(is_palindrome('zbcd'), False)

if __name__ == '__main__':
    unittest.main()