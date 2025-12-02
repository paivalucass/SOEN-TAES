def max_aggregate(stdata):
    if not stdata:
        return None

    from collections import defaultdict
    aggregate_dict = defaultdict(int)

    for name, score in stdata:
        if not isinstance(score, int):
            return "Error: Invalid input data"
        aggregate_dict[name] += score

    max_name = max(aggregate_dict, key=aggregate_dict.get)
    return (max_name, aggregate_dict[max_name])
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(max_aggregate([('Juan Whelan',90),('Sabah Colley',88),('Peter Nichols',7),('Juan Whelan',122),('Sabah Colley',84)]),('Juan Whelan', 212))

if __name__ == '__main__':
    unittest.main()