def remove_uppercase(str1):
    if str1 == '' or str1.isupper():
        return "Error: Input string cannot be empty or contain only uppercase characters"
    
    modified_str = ''
    for char in str1:
        if not char.isupper():
            modified_str += char
    
    return modified_str

# Test cases
assert remove_uppercase('cAstyoUrFavoRitETVshoWs') == 'cstyoravoitshos'
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(remove_uppercase('cAstyoUrFavoRitETVshoWs'), 'cstyoravoitshos')

if __name__ == '__main__':
    unittest.main()