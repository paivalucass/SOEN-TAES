def reverse_string_list(stringlist):
    if not isinstance(stringlist, list):
        raise ValueError("Input must be a list")
    for string in stringlist:
        if not isinstance(string, str):
            raise ValueError("All elements in the list must be strings")

    return [string[::-1] for string in stringlist]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(reverse_string_list(['Red', 'Green', 'Blue', 'White', 'Black']), ['deR', 'neerG', 'eulB', 'etihW', 'kcalB'])

if __name__ == '__main__':
    unittest.main()