import re

def remove_uppercase(str1):
    if not str1:
        return "Error: Input string is empty"
    else:
        new_str = re.sub(r'[A-Z]', '', str1)
        return new_str
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(remove_uppercase('cAstyoUrFavoRitETVshoWs'), 'cstyoravoitshos')

if __name__ == '__main__':
    unittest.main()