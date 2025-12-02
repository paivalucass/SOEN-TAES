def list_sort(lst):
    lst = [word for word in lst if len(word) % 2 == 0]
    lst.sort(key=lambda x: (len(x), x))
    return lst
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(list_sort(["aa", "a", "aaa"]), ["aa"])
        self.assertEqual(list_sort(["ab", "a", "aaa", "cd"]), ["ab", "cd"])

if __name__ == '__main__':
    unittest.main()