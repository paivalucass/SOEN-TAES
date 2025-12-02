def flip_case(string: str) -> str:
    if string is None or len(string) == 0:
        return "Input string is empty or None"
    
    return ''.join([char.lower() if char.isupper() else char.upper() for char in string])
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(flip_case('Hello'), 'hELLO')

if __name__ == '__main__':
    unittest.main()