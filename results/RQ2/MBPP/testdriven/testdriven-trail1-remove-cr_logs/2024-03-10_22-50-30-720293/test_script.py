import re

# Rewrite the code to fix the bug

def check_str(string): 
    pattern = r'^[aeiouAEIOU].*'
    return bool(re.match(pattern, string))
import re

class Test(unittest.TestCase):
    def test(self):
        self.assertTrue(check_str('annie'))

if __name__ == '__main__':
    unittest.main()