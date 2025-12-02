from collections import defaultdict

def max_aggregate(stdata):
    aggregate_dict = defaultdict(int)

    for name, score in stdata:
        aggregate_dict[name] += score
    
    max_aggregate = max(aggregate_dict.items(), key=lambda x: x[1])
    
    return max_aggregate
import unittest

class Test(unittest.TestCase):
    def test_max_aggregate(self):
        self.assertEqual(max_aggregate([('Juan Whelan',90),('Sabah Colley',88),('Peter Nichols',7),('Juan Whelan',122),('Sabah Colley',84)]), ('Juan Whelan', 212))

if __name__ == '__main__':
    unittest.main()