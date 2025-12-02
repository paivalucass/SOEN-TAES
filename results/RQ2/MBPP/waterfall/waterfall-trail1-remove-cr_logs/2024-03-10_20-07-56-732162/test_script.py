def is_lower(string):
    if not isinstance(string, str):
        raise TypeError("Input must be a string")
    
    try:
        lower_string = string.lower()
        return lower_string
    except AttributeError:
        raise ValueError("Invalid input")

# Test case
assert is_lower("InValid") == "invalid"
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_lower('InValid'), 'invalid')

if __name__ == '__main__':
    unittest.main()