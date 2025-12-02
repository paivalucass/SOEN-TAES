def max_of_nth(test_list, N):
    if not test_list or N < 0:
        raise ValueError

    max_value = float('-inf')
    for sublist in test_list:
        if len(sublist) > N:
            max_value = max(max_value, sublist[N])
    return max_value
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(max_of_nth([[5, 6, 7], [1, 3, 5], [8, 9, 19]], 2), 19)

if __name__ == '__main__':
    unittest.main()