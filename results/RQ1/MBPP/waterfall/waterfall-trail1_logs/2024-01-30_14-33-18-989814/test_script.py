def remove_uppercase(str1):
    modified_str = ''.join(filter(lambda x: not x.isupper(), str1))
    return modified_str
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(remove_uppercase('cAstyoUrFavoRitETVshoWs'), 'cstyoravoitshos')

if __name__ == '__main__':
    unittest.main()