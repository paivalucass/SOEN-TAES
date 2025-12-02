def is_palindrome(text: str) -> bool:
    if text is None:
        return True
    text = ''.join(e for e in text if e.isalnum()).lower()
    return text == text[::-1]

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_palindrome(''), True)
        self.assertEqual(is_palindrome('aba'), True)
        self.assertEqual(is_palindrome('aaaaa'), True)
        self.assertEqual(is_palindrome('zbcd'), False)

if __name__ == '__main__':
    unittest.main()