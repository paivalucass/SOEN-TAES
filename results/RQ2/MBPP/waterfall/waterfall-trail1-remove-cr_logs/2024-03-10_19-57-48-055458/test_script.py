def count_X(tup, x):
    count_dict = {}
    for element in tup:
        if isinstance(element, tuple):
            for sub_element in element:
                count_dict[sub_element] = count_dict.get(sub_element, 0) + 1
        else:
            count_dict[element] = count_dict.get(element, 0) + 1
    return count_dict.get(x, 0)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(count_X((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2), 4), 0)

if __name__ == '__main__':
    unittest.main()