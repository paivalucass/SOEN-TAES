def list_sort(lst):
    filtered_list = [word for word in lst if len(word) % 2 == 0]
    sorted_list = sorted(filtered_list, key=lambda x: (len(x), x))
    return sorted_list
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(list_sort(["aa", "a", "aaa"]), ["aa"])
        self.assertEqual(list_sort(["ab", "a", "aaa", "cd"]), ["ab", "cd"])

if __name__ == '__main__':
    unittest.main()