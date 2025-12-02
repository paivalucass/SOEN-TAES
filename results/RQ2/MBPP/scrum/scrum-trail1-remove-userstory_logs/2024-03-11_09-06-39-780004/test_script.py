def max_aggregate(stdata):
    from collections import defaultdict

    if not isinstance(stdata, list):
        return "Invalid input data format"

    aggregate_scores = defaultdict(int)

    for name, score in stdata:
        if not isinstance(name, str) or not isinstance(score, int):
            return "Invalid data type found"
        aggregate_scores[name] += score

    max_score = 0
    max_individual = ''
    for name, score in aggregate_scores.items():
        if score > max_score:
            max_score = score
            max_individual = name

    return (max_individual, max_score)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(max_aggregate([('Juan Whelan',90),('Sabah Colley',88),('Peter Nichols',7),('Juan Whelan',122),('Sabah Colley',84)]), ('Juan Whelan', 212))

if __name__ == '__main__':
    unittest.main()