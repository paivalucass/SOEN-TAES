def max_aggregate(stdata):
    import heapq
    from collections import defaultdict
    
    if not stdata:
        return None

    aggregate_dict = defaultdict(int)
    
    for name, value in stdata:
        if isinstance(value, int):
            aggregate_dict[name] += value
        else:
            raise ValueError

    max_aggregate = heapq.nlargest(1, aggregate_dict.items(), key=lambda x: x[1])
    
    return max_aggregate[0] if max_aggregate else None
import unittest

class Test(unittest.TestCase):
    def test_max_aggregate(self):
        self.assertEqual(max_aggregate([('Juan Whelan',90),('Sabah Colley',88),('Peter Nichols',7),('Juan Whelan',122),('Sabah Colley',84)]), ('Juan Whelan', 212))

if __name__ == '__main__':
    unittest.main()