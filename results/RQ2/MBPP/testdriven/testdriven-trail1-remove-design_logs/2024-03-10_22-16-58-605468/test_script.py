import re

def check_str(string):
    if string is None or string == "":
        return False
    pattern = r'^[aeiouAEIOU].*'
    return bool(re.match(pattern, string))
import re

class Test(unittest.TestCase):
    def test(self):
        self.assertTrue(check_str('annie'))

if __name__ == '__main__':
    unittest.main()