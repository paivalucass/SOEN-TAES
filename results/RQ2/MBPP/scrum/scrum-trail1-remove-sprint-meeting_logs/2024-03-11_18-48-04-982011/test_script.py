def remove_whitespaces(text):
    import re
    return re.sub(r'\s', '', text)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(remove_whitespaces(' Google    Flutter '), 'GoogleFlutter')

if __name__ == '__main__':
    unittest.main()