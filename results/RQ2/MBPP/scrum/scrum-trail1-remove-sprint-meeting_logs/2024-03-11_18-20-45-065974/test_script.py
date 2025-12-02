def check_integer(text):
    if text.strip() == '':
        return False
    if text[0] == '-' or text[0] == '+':
        return text[1:].isdigit()
    return text.isdigit()
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(check_integer('python'), False)

if __name__ == '__main__':
    unittest.main()