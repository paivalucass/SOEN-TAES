def remove_uppercase(str1):
    return ''.join(char for char in str1 if not char.isupper())
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(remove_uppercase('cAstyoUrFavoRitETVshoWs'), 'cstyoravoitshos')

if __name__ == '__main__':
    unittest.main()