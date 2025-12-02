def string_to_tuple(str1):
    if not isinstance(str1, str):
        raise ValueError("Input must be a string")
        
    if str1 is None or len(str1) == 0:
        return ()

    char_tuple = tuple(str1)

    return char_tuple
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(string_to_tuple("python 3.0"), ('p', 'y', 't', 'h', 'o', 'n', ' ', '3', '.', '0'))

if __name__ == '__main__':
    unittest.main()