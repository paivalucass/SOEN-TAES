def count_charac(str1):
    if not isinstance(str1, str):
        return "Error: Input is not a string"
    
    count = sum(1 for char in str1 if char.isalnum())
    return count
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(count_charac('python programming'), 18)

if __name__ == '__main__':
    unittest.main()