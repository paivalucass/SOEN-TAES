def reverse_string_list(stringlist):
    if not isinstance(stringlist, list):
        raise ValueError("Input should be a list")

    for string in stringlist:
        if not isinstance(string, str):
            raise ValueError("List should only contain strings")

    for i in range(len(stringlist)):
        stringlist[i] = stringlist[i][::-1]

    return stringlist
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(reverse_string_list(['Red', 'Green', 'Blue', 'White', 'Black']), ['deR', 'neerG', 'eulB', 'etihW', 'kcalB'])

if __name__ == '__main__':
    unittest.main()