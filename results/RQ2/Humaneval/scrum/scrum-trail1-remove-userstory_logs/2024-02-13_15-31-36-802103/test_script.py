def string_to_md5(text):
    if not isinstance(text, str) or text == "":
        return None
    
    import hashlib
    
    try:
        text_bytes = text.encode('utf-8')
        md5_hash = hashlib.md5(text_bytes).hexdigest()
        return md5_hash
    except UnicodeEncodeError:
        return None
import unittest
import hashlib

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(string_to_md5('Hello world'), '3e25960a79dbc69b674cd4ec67a72c62')
        self.assertEqual(string_to_md5(''), None)

if __name__ == '__main__':
    unittest.main()