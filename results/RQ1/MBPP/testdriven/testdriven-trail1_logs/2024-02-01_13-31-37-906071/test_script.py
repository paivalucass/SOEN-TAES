def text_starta_endb(text):
    if len(text) < 2:
        return False
    elif text[0] == 'a' and text[-1] == 'b':
        return True
    else:
        return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertTrue(text_starta_endb("aabbbb"))

if __name__ == '__main__':
    unittest.main()