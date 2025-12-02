def count_charac(str1):
    if str1 is None:
        return "Error"
    if not isinstance(str1, str):
        return "Error"
    return len(str1)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(count_charac('python programming'), 18)

if __name__ == '__main__':
    unittest.main()