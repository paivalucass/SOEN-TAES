def count_Pairs(input_list, n):
    # Error handling for empty or single-element input list
    if len(input_list) < 2:
        return 0

    # Use a dictionary to store the count of each unique integer in the list
    num_count = {}
    for num in input_list:
        if num in num_count:
            num_count[num] += 1
        else:
            num_count[num] = 1

    # Calculate the count of pairs using the combination formula for unordered pairs
    pairs_count = 0
    for num, count in num_count.items():
        pairs_count += (count * (n - count))

    return pairs_count // 2
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(count_Pairs([1,2,1],3), 2)

if __name__ == '__main__':
    unittest.main()