def find_length(string):
    max_diff = 0
    count = 0
    diff_map = {0: -1}
    for i in range(len(string)):
        count += 1 if string[i] == '1' else -1
        if count in diff_map:
            max_diff = max(max_diff, i - diff_map[count])
        else:
            diff_map[count] = i
    return max_diff

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_length('11000010001'), 6)

if __name__ == '__main__':
    unittest.main()