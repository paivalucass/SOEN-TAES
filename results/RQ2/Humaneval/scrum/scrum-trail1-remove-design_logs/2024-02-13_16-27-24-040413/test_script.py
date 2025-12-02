def sorted_list_sum(lst):
    def filter_odd_length_strings(lst):
        return [word for word in lst if len(word) % 2 == 0]

    def sort_strings(lst):
        return sorted(lst, key=lambda x: (len(x), x))

    filtered_list = filter_odd_length_strings(lst)
    sorted_list = sort_strings(filtered_list)
    
    return sorted_list
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sorted_list_sum(["aa", "a", "aaa"]), ["aa"])
        self.assertEqual(sorted_list_sum(["ab", "a", "aaa", "cd"]), ["ab", "cd"])

if __name__ == '__main__':
    unittest.main()