def flip_case(string: str) -> str:
    if not isinstance(string, str):
        raise ValueError("Input is not a valid string")
    
    output = ""
    for char in string:
        if char.islower():
            output += char.upper()
        else:
            output += char.lower()
    return output
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(flip_case('Hello'), 'hELLO')

if __name__ == '__main__':
    unittest.main()