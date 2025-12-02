def check_integer(text):
    if not isinstance(text, str):
        return False
    
    text = text.strip()  # Remove leading and trailing whitespaces
    
    if text == "":
        return False
    
    # Use regular expressions to check if the text consists of only numerical characters
    if text.isdigit():
        return True
    else:
        return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(check_integer('python'), False)

if __name__ == '__main__':
    unittest.main()