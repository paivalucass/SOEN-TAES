def count_Pairs(inputArray, size): 
    # Write a python function which takes a list of integers and counts the number of possible unordered pairs where both elements are unequal.
    # assert count_Pairs([1,2,1],3) == 2
    pairs = 0
    count = {}
    for num in inputArray:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    for key in count:
        pairs += (count[key] * (size - count[key]))
    return pairs // 2
import unittest

class Test(unittest.TestCase):
    def test_count_Pairs(self):
        self.assertEqual(count_Pairs([1,2,1],3), 2)

if __name__ == '__main__':
    unittest.main()