from typing import List

def sorted_list_sum(lst: List[str]) -> List[str]:
    lst = [word for word in lst if len(word) % 2 == 0]
    lst.sort(key=lambda x: (len(x), x))
    return lst
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sorted_list_sum(["aa", "a", "aaa"]), ["aa"])
        self.assertEqual(sorted_list_sum(["ab", "a", "aaa", "cd"]), ["ab", "cd"])

if __name__ == '__main__':
    unittest.main()