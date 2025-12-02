def ascii_value(k):
    """
    Function to find the ascii value of a character
    :param k: a character for which the ascii value needs to be found
    :return: The ascii value of the input character
    """
    if len(k) != 1:
        raise ValueError("Input must be a single character")
    # Get the ascii value of the input character
    return ord(k)

# Test the function
assert ascii_value('A') == 65
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(ascii_value('A'), 65)

if __name__ == '__main__':
    unittest.main()