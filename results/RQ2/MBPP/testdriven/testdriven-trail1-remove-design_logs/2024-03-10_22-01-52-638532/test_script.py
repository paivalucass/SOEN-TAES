def count_charac(str1):
    if not isinstance(str1, str):
        raise ValueError("Input must be a string")
    return len(str1.strip())
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(count_charac('python programming'), 18)

if __name__ == '__main__':
    unittest.main()