def string_to_md5(text):
    if text:
        hashed_text = hashlib.md5(text.encode()).hexdigest()
        return hashed_text
    else:
        return None
import unittest
import hashlib

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(string_to_md5('Hello world'), '3e25960a79dbc69b674cd4ec67a72c62')
        self.assertEqual(string_to_md5(''), None)

if __name__ == '__main__':
    unittest.main()