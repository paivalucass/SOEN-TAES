def count_Occurrence(tup, lst):
    from collections import defaultdict
    count_dict = defaultdict(int)

    try:
        for item in lst:
            count_dict[item] += tup.count(item)
    except (AttributeError, TypeError):
        return "Invalid input"

    return sum(count_dict.values())
import unittest

class Test(unittest.TestCase):
    def test_count_Occurrence(self):
        self.assertEqual(count_Occurrence(('a', 'a', 'c', 'b', 'd'),['a', 'b']), 3)

if __name__ == '__main__':
    unittest.main()