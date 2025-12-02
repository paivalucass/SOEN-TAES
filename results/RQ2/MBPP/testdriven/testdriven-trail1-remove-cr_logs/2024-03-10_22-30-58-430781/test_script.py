def check_integer(text):
    import re
    pattern = r'^[-+]?[0-9]+$'
    if re.match(pattern, text):
        return True
    else:
        return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(check_integer('python'), False)

if __name__ == '__main__':
    unittest.main()