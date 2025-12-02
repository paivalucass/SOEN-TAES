def odd_values_string(input_string):
    if input_string is None or len(input_string) == 0:
        return "Input string is empty or null"

    result = ""
    for index in range(len(input_string)):
        if index % 2 == 0:
            result += input_string[index]

    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(odd_values_string('abcdef'), 'ace')

if __name__ == '__main__':
    unittest.main()