def count_reverse_pairs(test_list):
    if not isinstance(test_list, list):
        raise TypeError("Input should be a list of strings")

    reverse_set = set()
    counter = 0
    for string in test_list:
        if string[::-1] in reverse_set:
            counter += 1
        else:
            reverse_set.add(string)

    return counter
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(count_reverse_pairs(["julia", "best", "tseb", "for", "ailuj"]), 2)

if __name__ == '__main__':
    unittest.main()