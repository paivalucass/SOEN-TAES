def string_to_md5(text):
    try:
        if not text:
            return None
        return hashlib.md5(text.encode()).hexdigest()
    except Exception as e:
        return f"Error: {e}"
import unittest
import hashlib

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(string_to_md5('Hello world'), '3e25960a79dbc69b674cd4ec67a72c62')
        self.assertEqual(string_to_md5(''), None)

if __name__ == '__main__':
    unittest.main()