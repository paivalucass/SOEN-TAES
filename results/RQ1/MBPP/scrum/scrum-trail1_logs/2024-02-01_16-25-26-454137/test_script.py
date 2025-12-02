def is_upper(string):
    import re
    try:
        if not re.match("^[a-zA-Z]+$", string):
            raise ValueError("Input string must consist of only alphabets")
        return string.upper()
    except ValueError as ve:
        return str(ve)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_upper('person'), "PERSON")

if __name__ == '__main__':
    unittest.main()