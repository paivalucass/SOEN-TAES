from collections import deque

def is_palindrome(text: str) -> bool:
    text = ''.join(filter(str.isalnum, text)).lower()
    queue = deque(text)
    while len(queue) > 1:
        if queue.popleft() != queue.pop():
            return False
    return True
import unittest

class Test(unittest.TestCase):
    def test_empty_string(self):
        self.assertTrue(is_palindrome(''))

    def test_palindrome(self):
        self.assertTrue(is_palindrome('aba'))
        self.assertTrue(is_palindrome('aaaaa'))

    def test_non_palindrome(self):
        self.assertFalse(is_palindrome('zbcd'))

if __name__ == '__main__':
    unittest.main()