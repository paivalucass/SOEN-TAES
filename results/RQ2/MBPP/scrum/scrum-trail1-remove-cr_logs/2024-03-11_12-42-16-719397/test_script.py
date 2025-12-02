def check_integer(text):
    if text == "":
        return False
    text = text.strip()
    if text[0] in ["+", "-"]:
        text = text[1:]
    for char in text:
        if char not in "0123456789":
            return False
    return True
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(check_integer('python'), False)

if __name__ == '__main__':
    unittest.main()