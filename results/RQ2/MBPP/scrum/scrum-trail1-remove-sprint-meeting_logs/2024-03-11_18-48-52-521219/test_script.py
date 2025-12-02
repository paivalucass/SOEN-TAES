def reverse_string_list(stringlist):
    if not isinstance(stringlist, list):
        raise TypeError("Input must be a list")

    for s in stringlist:
        if not isinstance(s, str):
            raise TypeError("All elements in the list must be strings")

    reversed_strings = [s[::-1] for s in stringlist]
    return reversed_strings
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(reverse_string_list(['Red', 'Green', 'Blue', 'White', 'Black']), ['deR', 'neerG', 'eulB', 'etihW', 'kcalB'])

if __name__ == '__main__':
    unittest.main()