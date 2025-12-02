def remove_uppercase(str1):
    '''
    Write a function to remove uppercase substrings from a given string.
    assert remove_uppercase('cAstyoUrFavoRitETVshoWs') == 'cstyoravoitshos'
    '''
    new_string = ""
    for char in str1:
        if char.islower():
            new_string += char
    return new_string
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(remove_uppercase('cAstyoUrFavoRitETVshoWs'), 'cstyoravoitshos')

if __name__ == '__main__':
    unittest.main()