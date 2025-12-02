def string_to_tuple(str1):
    if str1 is None or not isinstance(str1, str):
        raise ValueError("Error: Input is not a valid string")

    if len(str1) == 0:
        return ()
    else:
        return tuple(str1)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(string_to_tuple('python 3.0'), ('p', 'y', 't', 'h', 'o', 'n', ' ', '3', '.', '0'))

if __name__ == '__main__':
    unittest.main()