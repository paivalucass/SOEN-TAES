def remove_whitespaces(text1):
    if not isinstance(text1, str):
        raise ValueError("Input should be a string")
    
    return ''.join(text1.split())
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(remove_whitespaces(' Google    Flutter '), 'GoogleFlutter')

if __name__ == '__main__':
    unittest.main()