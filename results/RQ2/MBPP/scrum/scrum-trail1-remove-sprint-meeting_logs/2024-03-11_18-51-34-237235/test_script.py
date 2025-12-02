def remove_lowercase(str1):
    import re
    if not isinstance(str1, str):
        raise ValueError("Input is not a string")
    
    pattern = r"[a-z]+"
    modified_string = re.sub(pattern, "", str1)
    
    return modified_string
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(remove_lowercase('PYTHon'), 'PYTH')

if __name__ == '__main__':
    unittest.main()