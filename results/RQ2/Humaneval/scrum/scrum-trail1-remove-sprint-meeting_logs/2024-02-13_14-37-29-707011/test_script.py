def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.
    """
    
    if text == "":
        return None
    
    import hashlib
    md5_hash = hashlib.md5(text.encode()).hexdigest()
    return md5_hash
import unittest
import hashlib

class Test(unittest.TestCase):
    def test_string_to_md5(self):
        self.assertEqual(string_to_md5('Hello world'), '3e25960a79dbc69b674cd4ec67a72c62')
        self.assertIsNone(string_to_md5(''))

if __name__ == '__main__':
    unittest.main()