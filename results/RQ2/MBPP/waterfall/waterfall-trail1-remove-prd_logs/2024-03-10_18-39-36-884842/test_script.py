def remove_uppercase(str1):
    newString = ''.join(filter(lambda x: x.islower(), str1))
    return newString
assert remove_uppercase('cAstyoUrFavoRitETVshoWs') == 'cstyoravoitshos'
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(remove_uppercase('cAstyoUrFavoRitETVshoWs'), 'cstyoravoitshos')

if __name__ == '__main__':
    unittest.main()