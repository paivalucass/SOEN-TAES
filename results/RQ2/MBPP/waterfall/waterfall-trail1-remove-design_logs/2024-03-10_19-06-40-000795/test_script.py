def check_integer(text):
    if text.strip() and text.lstrip('-').isdigit():
        return True
    return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(check_integer('python'), False)

if __name__ == '__main__':
    unittest.main()