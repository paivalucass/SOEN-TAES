def remove_uppercase(input_string: str) -> str:
    result = ""
    for char in input_string:
        if not char.isupper():
            result += char
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(remove_uppercase('cAstyoUrFavoRitETVshoWs'), 'cstyoravoitshos')

if __name__ == '__main__':
    unittest.main()