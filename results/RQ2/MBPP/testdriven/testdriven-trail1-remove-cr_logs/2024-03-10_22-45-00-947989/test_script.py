def empty_list(length):
    """
    Function to create a list of N empty dictionaries
    :param length: Length of the list (N)
    :return: List of N empty dictionaries
    """
    # Input validation to ensure that N is a positive integer
    if not isinstance(length, int) or length <= 0:
        raise ValueError("Length should be a positive integer")

    # Create a list of N empty dictionaries
    return [{} for _ in range(length)]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(empty_list(5), [{},{},{},{},{}])

if __name__ == '__main__':
    unittest.main()