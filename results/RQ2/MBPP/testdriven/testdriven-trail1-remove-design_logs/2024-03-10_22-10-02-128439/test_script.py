def check_value(dictionary, n):
    """
    Function to check if all values are the same in a dictionary.
    
    Args:
    dictionary: A dictionary to check
    n: A value to compare with
    
    Returns:
    True if all values are the same, False otherwise
    """
    values = list(dictionary.values())
    return all(value == values[0] for value in values) if values else False

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(check_value({'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra Gentry': 12, 'Pierre Cox': 12}, 10), False)

if __name__ == '__main__':
    unittest.main()