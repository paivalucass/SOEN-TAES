def check_integer(text):
    if text.isdigit():
        return True
    else:
        return False

assert check_integer("")==False
assert check_integer("123")==True
assert check_integer("-2147483649")==False
assert check_integer("123")==True
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(check_integer('python'), False)

if __name__ == '__main__':
    unittest.main()