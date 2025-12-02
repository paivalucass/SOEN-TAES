import re
def string_to_tuple(str1):
    try:
        if not str1:
            raise ValueError("Input string is empty or null")

        str1 = re.sub(r'[^a-zA-Z0-9]', '', str1)
        return tuple(str1)
    except Exception as e:
        raise e
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(string_to_tuple('python 3.0'), ('p', 'y', 't', 'h', 'o', 'n', ' ', '3', '.', '0'))

if __name__ == '__main__':
    unittest.main()