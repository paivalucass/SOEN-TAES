def reverse_string_list(stringlist):
    if not all(isinstance(s, str) for s in stringlist):
        raise ValueError('Input must be a list of strings')
    
    if stringlist is None:
        return "Error: Input is null"

    reversed_list = [string[::-1] for string in stringlist]
    return reversed_list
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(reverse_string_list(['Red', 'Green', 'Blue', 'White', 'Black']), ['deR', 'neerG', 'eulB', 'etihW', 'kcalB'])

if __name__ == '__main__':
    unittest.main()