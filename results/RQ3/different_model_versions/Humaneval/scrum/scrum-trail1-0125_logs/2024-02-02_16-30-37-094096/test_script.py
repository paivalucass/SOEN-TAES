def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """

    if not text:
        return None
    
    import hashlib
    return hashlib.md5(text.encode()).hexdigest()
import unittest
import hashlib

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(string_to_md5('Hello world'), '3e25960a79dbc69b674cd4ec67a72c62')
        self.assertIsNone(string_to_md5(''))

if __name__ == '__main__':
    unittest.main()