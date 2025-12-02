def list_sort(lst):
    if not isinstance(lst, list):
        raise TypeError("Input parameter must be a list of strings")

    if not lst:
        raise ValueError("Input list is empty")

    result = [word for word in lst if len(word) % 2 == 0]
    result.sort(key=lambda x: (len(x), x))
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(list_sort(["aa", "a", "aaa"]), ["aa"])
        self.assertEqual(list_sort(["ab", "a", "aaa", "cd"]), ["ab", "cd"])

if __name__ == '__main__':
    unittest.main()