def strlen(string: str) -> int:
    """
    Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """
    if not isinstance(string, str) or string is None:
        raise ValueError("Input should be a non-empty string")

    return len(string)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(strlen(''), 0)
        self.assertEqual(strlen('abc'), 3)

if __name__ == '__main__':
    unittest.main()