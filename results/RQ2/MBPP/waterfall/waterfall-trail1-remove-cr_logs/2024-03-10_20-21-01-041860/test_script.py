def find_length(string):
    max_diff = 0
    count = 0
    diff_dict = {0: -1}
    for i in range(len(string)):
        if string[i] == '0':
            count += 1
        else:
            count -= 1
        if count in diff_dict:
            max_diff = max(max_diff, i - diff_dict[count])
        else:
            diff_dict[count] = i
    return max_diff
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_length('11000010001'), 6)

if __name__ == '__main__':
    unittest.main()