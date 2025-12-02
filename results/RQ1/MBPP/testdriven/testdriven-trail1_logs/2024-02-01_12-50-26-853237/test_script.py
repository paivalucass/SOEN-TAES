def remove_uppercase(str1):
    import re
    return re.sub(r'[A-Z]', '', str1)

assert remove_uppercase('cAstyoUrFavoRitETVshoWs') == 'cstyoravoitshos'
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(remove_uppercase('cAstyoUrFavoRitETVshoWs'), 'cstyoravoitshos')

if __name__ == '__main__':
    unittest.main()