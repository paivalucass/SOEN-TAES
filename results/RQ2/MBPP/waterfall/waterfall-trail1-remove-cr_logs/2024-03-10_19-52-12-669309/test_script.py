def len_log(list1):
    if not list1:
        raise ValueError("Input list cannot be empty")

    longest_word_length = 0
    for word in list1:
        if not word.isalpha():
            raise ValueError("Input list contains special characters or numbers")
        if len(word) > longest_word_length:
            longest_word_length = len(word)
    return longest_word_length

# Test Cases:
{
  "test_cases": [
    {
      "Test Title": "Valid Input List - Edge Cases",
      "Input Data": "list1=['python','PHP','bigdata']",
      "Expected Output": 7
    },
    {
      "Test Title": "Empty Input List - Edge Cases",
      "Input Data": "list1=[]",
      "Expected Output": "ValueError"
    },
    {
      "Test Title": "List with Special Characters and Numbers - Edge Cases",
      "Input Data": "list1=['123', '456', '789']",
      "Expected Output": "ValueError"
    },
    {
      "Test Title": "Large Input List - Edge Cases",
      "Input Data": "list1=['a'*1000000]",
      "Expected Output": "1000000"
    }
  ]
}
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(len_log(["python","PHP","bigdata"]), 7)

if __name__ == '__main__':
    unittest.main()