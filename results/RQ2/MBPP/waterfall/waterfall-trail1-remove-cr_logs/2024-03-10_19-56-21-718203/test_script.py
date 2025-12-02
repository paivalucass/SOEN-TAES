def odd_values_string(input_string):
    if input_string is None or input_string == "":
        return "Error: Input string is empty or None"

    result = ""
    for index, char in enumerate(input_string):
        if index % 2 == 0:
            result += char
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(odd_values_string('abcdef'), 'ace')

if __name__ == '__main__':
    unittest.main()