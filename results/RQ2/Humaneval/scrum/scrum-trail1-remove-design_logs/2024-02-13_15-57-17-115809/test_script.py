def flip_case(string: str) -> str:
    return ''.join([char.lower() if char.isupper() else char.upper() for char in string])
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(flip_case('Hello'), 'hELLO')

if __name__ == '__main__':
    unittest.main()