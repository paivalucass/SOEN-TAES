def sorted_list_sum(lst):
    filtered_list = [string for string in lst if len(string) % 2 == 0]
    sorted_list = sorted(filtered_list, key=lambda x: (len(x), x))
    return sorted_list
import unittest

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(sorted_list_sum(["aa", "a", "aaa"]), ["aa"])

    def test2(self):
        self.assertEqual(sorted_list_sum(["ab", "a", "aaa", "cd"]), ["ab", "cd"])

if __name__ == '__main__':
    unittest.main()