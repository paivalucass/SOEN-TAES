def count_charac(str1):
    # Write a function to count the total number of characters in a string
    return len(str1)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(count_charac('python programming'), 18)

if __name__ == '__main__':
    unittest.main()