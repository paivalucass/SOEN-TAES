def unique_sublists(list1):
    if not all(isinstance(sublist, list) for sublist in list1):
        raise ValueError("Input must be a list of lists")

    sublists_count = {}
    for sublist in list1:
        sublists_count[tuple(sublist)] = sublists_count.get(tuple(sublist), 0) + 1

    return sublists_count
import unittest

class Test(unittest.TestCase):
    def test_unique_sublists(self):
        self.assertEqual(unique_sublists([[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7], [9, 11]]), {(1, 3): 2, (5, 7): 2, (13, 15, 17): 1, (9, 11): 1})

if __name__ == '__main__':
    unittest.main()