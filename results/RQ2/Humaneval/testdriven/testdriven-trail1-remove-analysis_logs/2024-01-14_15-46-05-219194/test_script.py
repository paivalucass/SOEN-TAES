def flip_case(string: str) -> str:
    if not isinstance(string, str):
        raise TypeError("Input must be a string")
    if not string:
        return ""

    result = ''.join([char.upper() if char.islower() else char.lower() if char.isupper() else char for char in string])

    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(flip_case('Hello'), 'hELLO')

if __name__ == '__main__':
    unittest.main()