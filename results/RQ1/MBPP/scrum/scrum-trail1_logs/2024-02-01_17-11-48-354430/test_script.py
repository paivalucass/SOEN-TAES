def check_integer(text):
    try:
        int(text.strip())
        return True
    except ValueError:
        return False
assert check_integer("python")==False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(check_integer('python'), False)

if __name__ == '__main__':
    unittest.main()