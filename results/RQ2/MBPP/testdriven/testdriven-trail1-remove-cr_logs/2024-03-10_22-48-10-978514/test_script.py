def largest_subset(numbers):
    if not numbers:
        return 0
    
    def find_divisible_pairs(numbers):
        divisible_pairs = []
        for i in range(len(numbers)):
            for j in range(i+1, len(numbers)):
                if numbers[i] % numbers[j] == 0 or numbers[j] % numbers[i] == 0:
                    divisible_pairs.append((numbers[i], numbers[j]))
        return divisible_pairs

    divisible_pairs = find_divisible_pairs(numbers)
    max_subset_size = 0
    for num in numbers:
        subset = [num]
        for pair in divisible_pairs:
            if num in pair and pair[0] not in subset:
                subset.append(pair[0])
            elif num in pair and pair[1] not in subset:
                subset.append(pair[1])
        max_subset_size = max(max_subset_size, len(subset))
    return max_subset_size

import unittest

class Test(unittest.TestCase):
    def test_largest_subset(self):
        self.assertEqual(largest_subset([1, 3, 6, 13, 17, 18]), 4)

if __name__ == '__main__':
    unittest.main()