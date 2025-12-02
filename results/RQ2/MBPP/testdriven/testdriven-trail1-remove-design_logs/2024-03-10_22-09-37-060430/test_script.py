def reverse_string_list(stringlist):
    if not isinstance(stringlist, list):
        raise ValueError("Input must be a list of strings")
    
    for s in stringlist:
        if not isinstance(s, str):
            raise ValueError("All elements in the list must be strings")
    
    return [s[::-1] for s in stringlist]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(reverse_string_list(['Red', 'Green', 'Blue', 'White', 'Black']), ['deR', 'neerG', 'eulB', 'etihW', 'kcalB'])

if __name__ == '__main__':
    unittest.main()