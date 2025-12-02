def check_integer(text):
    try:
        if text is None or text == "":
            return False
        return text.lstrip('-+').isdigit()
    except AttributeError:
        return False

# Test the function with different input scenarios
print(check_integer(""))  # False
print(check_integer("123"))  # True
print(check_integer("abc"))  # False
print(check_integer("python"))  # False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(check_integer('python'), False)

if __name__ == '__main__':
    unittest.main()