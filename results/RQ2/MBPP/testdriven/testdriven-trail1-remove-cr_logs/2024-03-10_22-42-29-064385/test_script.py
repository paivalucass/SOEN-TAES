def remove_whitespaces(text1):
    return ''.join(text1.split())

assert remove_whitespaces(' Google    Flutter ') == 'GoogleFlutter'
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(remove_whitespaces(' Google    Flutter '), 'GoogleFlutter')

if __name__ == '__main__':
    unittest.main()