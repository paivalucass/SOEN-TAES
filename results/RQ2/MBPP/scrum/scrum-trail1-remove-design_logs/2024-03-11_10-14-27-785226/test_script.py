def odd_values_string(input_string):
    if len(input_string) < 2:
        return "Error: Input string is empty or has a length less than 2"

    result = ""
    for index in range(len(input_string)):
        if index % 2 == 0:
            result += input_string[index]

    return result
import unittest

class Test(unittest.TestCase):
    def test_odd_values_string(self):
        self.assertEqual(odd_values_string('abcdef'), 'ace')

if __name__ == '__main__':
    unittest.main()