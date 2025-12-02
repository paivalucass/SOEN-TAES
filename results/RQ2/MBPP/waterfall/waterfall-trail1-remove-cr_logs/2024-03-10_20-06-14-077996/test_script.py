def remove_whitespaces(text1):
    modified_text = "".join(text1.split())
    return modified_text
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(remove_whitespaces(' Google    Flutter '), 'GoogleFlutter')

if __name__ == '__main__':
    unittest.main()