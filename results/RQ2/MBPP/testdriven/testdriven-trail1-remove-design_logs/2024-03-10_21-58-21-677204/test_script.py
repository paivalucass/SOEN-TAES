def check_integer(text):
    try:
        int(text)
        return True
    except ValueError:
        return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(check_integer('python'), False)

if __name__ == '__main__':
    unittest.main()