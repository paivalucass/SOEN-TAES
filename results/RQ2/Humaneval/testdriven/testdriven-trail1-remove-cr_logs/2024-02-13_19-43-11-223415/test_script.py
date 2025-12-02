def flip_case(string: str) -> str:
    if string is None:
        return None
    elif not isinstance(string, str):
        return "Input is not a string"

    result = ""
    for char in string:
        if char.islower():
            result += char.upper()
        elif char.isupper():
            result += char.lower()
        else:
            result += char

    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(flip_case('Hello'), 'hELLO')

if __name__ == '__main__':
    unittest.main()