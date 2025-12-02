def combinations_colors(l, n):
    result = []
    def find_combinations(current_combination, start_index):
        if len(current_combination) == n:
            result.append(tuple(current_combination))
            return
        for i in range(start_index, len(l)):
            find_combinations(current_combination + [l[i]], i)
    find_combinations([], 0)
    return result
import unittest

class Test(unittest.TestCase):
    def test_combinations_colors(self):
        self.assertEqual(combinations_colors(["Red","Green","Blue"], 1), [('Red',), ('Green',), ('Blue',)])

if __name__ == '__main__':
    unittest.main()