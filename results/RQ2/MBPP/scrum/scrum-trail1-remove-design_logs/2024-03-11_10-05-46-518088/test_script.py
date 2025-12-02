def check_integer(text):
    try:
        int(text)
        return True
    except ValueError:
        return False

# Test cases
assert check_integer("") == False
assert check_integer("123") == True
assert check_integer("abc") == False
assert check_integer("-123") == True
assert check_integer("9999999999999999") == True
assert check_integer("0") == True
assert check_integer("-123") == True
assert check_integer("-456") == True
assert check_integer("!@#$%") == False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(check_integer('python'), False)

if __name__ == '__main__':
    unittest.main()