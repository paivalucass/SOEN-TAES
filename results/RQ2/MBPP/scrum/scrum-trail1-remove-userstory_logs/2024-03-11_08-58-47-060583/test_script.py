def odd_values_string(input_str):
    result = "".join([input_str[i] for i in range(len(input_str)) if i % 2 == 0])
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(odd_values_string('abcdef'), 'ace')

if __name__ == '__main__':
    unittest.main()