def test_three_equal(x, y, z):
    numbers = [x, y, z]
    occurrences = {}
    for num in numbers:
        if num in occurrences:
            occurrences[num] += 1
        else:
            occurrences[num] = 1
    max_occurrences = max(occurrences.values())
    return max_occurrences
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(test_three_equal(1, 1, 1), 3)

if __name__ == '__main__':
    unittest.main()