def is_lower(string):
    return string.lower() == string.lower()
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_lower('InValid'), "invalid")

if __name__ == '__main__':
    unittest.main()