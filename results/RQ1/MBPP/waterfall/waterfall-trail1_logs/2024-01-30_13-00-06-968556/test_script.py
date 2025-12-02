def max_aggregate(stdata):
    # Input validation
    if not isinstance(stdata, list) or not all(isinstance(item, tuple) for item in stdata):
        raise ValueError("Input stdata must be a list of tuples")

    # Use a dictionary to keep track of aggregate scores for each name
    aggregate_scores = {}
    for name, score in stdata:
        if score < 0:
            raise ValueError("Negative scores are not allowed")
        aggregate_scores[name] = aggregate_scores.get(name, 0) + score

    # Find the maximum aggregate and corresponding name
    max_name = None
    max_aggregate_value = float('-inf')
    for name, aggregate in aggregate_scores.items():
        if aggregate > max_aggregate_value:
            max_name = name
            max_aggregate_value = aggregate

    # Handle empty input lists
    if not stdata:
        return None

    return max_name, max_aggregate_value
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(max_aggregate([('Juan Whelan',90),('Sabah Colley',88),('Peter Nichols',7),('Juan Whelan',122),('Sabah Colley',84)]),('Juan Whelan', 212))

if __name__ == '__main__':
    unittest.main()