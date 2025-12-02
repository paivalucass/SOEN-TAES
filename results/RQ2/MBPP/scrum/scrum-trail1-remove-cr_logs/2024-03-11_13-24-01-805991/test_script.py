def reverse_string_list(stringlist):
    reversed_list = []
    for string in stringlist:
        reversed_string = string[::-1]
        reversed_list.append(reversed_string)
    return reversed_list
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(reverse_string_list(['Red', 'Green', 'Blue', 'White', 'Black']), ['deR', 'neerG', 'eulB', 'etihW', 'kcalB'])

if __name__ == '__main__':
    unittest.main()