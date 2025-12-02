def string_to_tuple(str1):
    if str1 == "" or str1 is None:
        return "Error: Invalid input"

    characters = [char for char in str1]
    return tuple(characters)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(string_to_tuple('python 3.0'), ('p', 'y', 't', 'h', 'o', 'n', ' ', '3', '.', '0'))

if __name__ == '__main__':
    unittest.main()