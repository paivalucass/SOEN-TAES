def max_aggregate(stdata):
    aggregate_scores = {}
    for name, score in stdata:
        if name in aggregate_scores:
            aggregate_scores[name] += score
        else:
            aggregate_scores[name] = score
    max_name = max(aggregate_scores, key=aggregate_scores.get)
    return (max_name, aggregate_scores[max_name])
import unittest

class Test(unittest.TestCase):
    def test_max_aggregate(self):
        self.assertEqual(max_aggregate([('Juan Whelan',90),('Sabah Colley',88),('Peter Nichols',7),('Juan Whelan',122),('Sabah Colley',84)]), ('Juan Whelan', 212))

if __name__ == '__main__':
    unittest.main()