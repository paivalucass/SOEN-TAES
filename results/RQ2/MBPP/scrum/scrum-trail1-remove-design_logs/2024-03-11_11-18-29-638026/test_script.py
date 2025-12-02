import re

def text_starta_endb(text):
    pattern = 'a.*b'
    if re.search(pattern, text):
        return True
    else:
        return False

assert text_starta_endb("aabbbb")
import re

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(text_starta_endb('aabbbb'), 1)

if __name__ == '__main__':
    unittest.main()