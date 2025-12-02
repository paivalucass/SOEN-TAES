def count_charac(str1):
    if str1 is None:
        return "Invalid input"
    else:
        return len(str1)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(count_charac('python programming'), 18)

if __name__ == '__main__':
    unittest.main()