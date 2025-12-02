def max_aggregate(stdata):
    if not isinstance(stdata, list) or any(not isinstance(item, tuple) or len(item) != 2 or not isinstance(item[0], str) or not (isinstance(item[1], int) or isinstance(item[1], float)) for item in stdata):
        return None

    aggregate_scores = {}
    for name, score in stdata:
        aggregate_scores[name] = aggregate_scores.get(name, 0) + score

    max_student = max(aggregate_scores, key=aggregate_scores.get)
    max_aggregate_score = aggregate_scores[max_student]

    return (max_student, max_aggregate_score)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(max_aggregate([('Juan Whelan',90),('Sabah Colley',88),('Peter Nichols',7),('Juan Whelan',122),('Sabah Colley',84)]),('Juan Whelan', 212))

if __name__ == '__main__':
    unittest.main()