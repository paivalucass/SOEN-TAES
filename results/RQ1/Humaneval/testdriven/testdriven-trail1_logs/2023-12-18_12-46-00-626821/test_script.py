def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """

    import hashlib
    if not text:
        return None
    try:
        md5_hash = hashlib.md5(text.encode()).hexdigest()
        return md5_hash
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
import unittest
import hashlib

class TestStringToMD5(unittest.TestCase):
    def test_non_empty_string(self):
        self.assertEqual(string_to_md5('Hello world'), '3e25960a79dbc69b674cd4ec67a72c62')

    def test_empty_string(self):
        self.assertIsNone(string_to_md5(''))

if __name__ == '__main__':
    unittest.main()