def sorted_list_sum(lst):
    result = sorted([word for word in lst if len(word) % 2 == 0], key=lambda x: (len(x), x))
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sorted_list_sum(["aa", "a", "aaa"]), ["aa"])
        self.assertEqual(sorted_list_sum(["ab", "a", "aaa", "cd"]), ["ab", "cd"])

if __name__ == '__main__':
    unittest.main()