def find_length(string):
    if not string:
        return "Error: Invalid input - empty string"
    count_of_0 = 0
    count_of_1 = 0
    max_difference = 0
    for char in string:
        if char != '0' and char != '1':
            return "Error: Invalid input - non-binary characters"
        if char == '0':
            count_of_0 += 1
        else:
            count_of_1 += 1
        difference = count_of_0 - count_of_1
        if difference > max_difference:
            max_difference = difference
    return abs(max_difference)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_length('11000010001'), 6)

if __name__ == '__main__':
    unittest.main()