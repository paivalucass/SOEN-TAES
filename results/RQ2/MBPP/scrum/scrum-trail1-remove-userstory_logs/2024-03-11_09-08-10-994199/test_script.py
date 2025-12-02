def max_length_list(input_list):
    if not input_list:
        return (0, [])

    max_length = 0
    max_list = []

    for sublist in input_list:
        if not isinstance(sublist, list):
            return "Invalid Input"

        if len(sublist) > max_length:
            max_length = len(sublist)
            max_list = sublist

    if max_list:
        return (max_length, max_list)
    else:
        return (0, [])
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(max_length_list([[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]), (3, [13, 15, 17]))

if __name__ == '__main__':
    unittest.main()