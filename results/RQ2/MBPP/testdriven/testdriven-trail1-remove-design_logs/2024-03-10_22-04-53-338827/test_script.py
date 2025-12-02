def max_aggregate(stdata):
    if not isinstance(stdata, list):
        return "Error: Invalid input. Input data must be a list of tuples."
    aggregated_scores = {}
    for name, score in stdata:
        if not isinstance(name, str) or not isinstance(score, int):
            return "Error: Invalid input format. Each tuple should contain a string and an integer."
        if score < 0:
            return "Error: Invalid input. Scores cannot be negative."
        if name in aggregated_scores:
            aggregated_scores[name] += score
        else:
            aggregated_scores[name] = score
    max_aggregate = max(aggregated_scores.items(), key=lambda x: x[1])
    return max_aggregate

import unittest

class Test(unittest.TestCase):
    def test_max_aggregate(self):
        self.assertEqual(max_aggregate([('Juan Whelan',90),('Sabah Colley',88),('Peter Nichols',7),('Juan Whelan',122),('Sabah Colley',84)]), ('Juan Whelan', 212))

if __name__ == '__main__':
    unittest.main()