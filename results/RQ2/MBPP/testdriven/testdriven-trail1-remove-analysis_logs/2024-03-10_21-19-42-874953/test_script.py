def remove_odd(input_string):
    # Remove odd characters in the input string
    result = ''.join(filter(lambda x: input_string.index(x) % 2 != 0, input_string))
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(remove_odd('python'), 'yhn')

if __name__ == '__main__':
    unittest.main()