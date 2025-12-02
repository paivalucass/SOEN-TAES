def remove_odd(input_string):
    '''This function removes odd characters from a given input string.'''
    result = ""
    for i in range(len(input_string)):
        if i % 2 == 1:
            result += input_string[i]
    return result

# Test cases
assert remove_odd("python") == "yhn"
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(remove_odd('python'), 'yhn')

if __name__ == '__main__':
    unittest.main()