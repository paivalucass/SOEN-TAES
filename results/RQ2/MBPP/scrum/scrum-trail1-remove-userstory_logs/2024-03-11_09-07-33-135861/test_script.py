def string_to_tuple(str1):
    if not isinstance(str1, str):
        raise TypeError("Input must be a string")
    if not str1:
        raise ValueError("Input string cannot be empty")
    
    return tuple(str1)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(string_to_tuple('python 3.0'), ('p', 'y', 't', 'h', 'o', 'n', ' ', '3', '.', '0'))

if __name__ == '__main__':
    unittest.main()