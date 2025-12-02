import unittest
import hashlib

def string_to_md5(text):
    if not text:
        return None
    return hashlib.md5(text.encode()).hexdigest()

class TestStringToMD5(unittest.TestCase):
    def test_string_to_md5(self):
        self.assertEqual(string_to_md5('Hello world'), '3e25960a79dbc69b674cd4ec67a72c62')

if __name__ == '__main__':
    unittest.main()
import hashlib

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(string_to_md5('Hello world'), '3e25960a79dbc69b674cd4ec67a72c62')

if __name__ == '__main__':
    unittest.main()