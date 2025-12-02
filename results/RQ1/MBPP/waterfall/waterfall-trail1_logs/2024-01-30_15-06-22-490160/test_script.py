def count_reverse_pairs(test_list):
    count = 0
    reverse_dict = {}
    for word in test_list:
        reverse_word = word[::-1]
        if reverse_word in reverse_dict:
            count += reverse_dict[reverse_word]
        if word in reverse_dict:
            reverse_dict[word] += 1
        else:
            reverse_dict[word] = 1
    return count

# Testing the function with different input lists
print(count_reverse_pairs(["ab", "ba", "abc", "cba"])) # Output: 2
print(count_reverse_pairs(["ab", "ba", "abc", "cba", "a"])) # Output: 3
print(count_reverse_pairs(["ab", "ba", "abc", "cba", "a", "ab"])) # Output: 4

# Test Cases:
{
  "test_cases": [
    {
      "Test Title": "Empty Input",
      "Input Data": "test_list=[]",
      "Expected Output": "0"
    },
    {
      "Test Title": "Single String Input",
      "Input Data": "test_list=['hello']",
      "Expected Output": "0"
    },
    {
      "Test Title": "Case Sensitive",
      "Input Data": "test_list=['abcd', 'dcba', 'ABCD']",
      "Expected Output": "1"
    },
    {
      "Test Title": "Special Characters",
      "Input Data": "test_list=['$#@', '#@$']",
      "Expected Output": "1"
    },
    {
      "Test Title": "Multiple Strings",
      "Input Data": "test_list=['abc', '123', 'ABc', '456', 'zyx', 'XyZ']",
      "Expected Output": "3"
    }
  ]
}
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(count_reverse_pairs(["julia", "best", "tseb", "for", "ailuj"]), 2)

if __name__ == '__main__':
    unittest.main()