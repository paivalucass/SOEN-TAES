def find_length(string):
    max_difference = 0
    count = 0
    count_map = {0: -1}

    for i in range(len(string)):
        if string[i] == '0':
            count -= 1
        else:
            count += 1

        if count in count_map:
            max_difference = max(max_difference, i - count_map[count])
        else:
            count_map[count] = i

    return max_difference
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_length("11000010001"), 6)

if __name__ == '__main__':
    unittest.main()