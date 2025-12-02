def find_max_difference(string):
    if not string:
        raise ValueError("Empty input string")

    max_difference = 0
    count_0 = 0
    count_1 = 0

    for char in string:
        if char != '0' and char != '1':
            raise ValueError("Invalid input: non-binary character found")

        if char == '0':
            count_0 += 1
        else:
            count_1 += 1

        difference = count_0 - count_1
        if difference > max_difference:
            max_difference = difference

    return max_difference
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_length("11000010001"), 6)

if __name__ == '__main__':
    unittest.main()