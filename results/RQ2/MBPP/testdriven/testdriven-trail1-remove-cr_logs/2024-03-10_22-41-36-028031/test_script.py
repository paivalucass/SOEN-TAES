def count_bidirectional(test_list):
    if not all(isinstance(item, tuple) and len(item) == 2 for item in test_list):
        return "Error Handling"

    count = 0
    for i in range(len(test_list)):
        for j in range(i + 1, len(test_list)):
            if test_list[i] == test_list[j][::-1]:
                count += 1

    return count

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(count_bidirectional([(5, 6), (1, 2), (6, 5), (9, 1), (6, 5), (2, 1)]), 3)

if __name__ == '__main__':
    unittest.main()