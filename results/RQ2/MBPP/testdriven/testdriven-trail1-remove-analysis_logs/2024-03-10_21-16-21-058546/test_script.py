def max_aggregate(stdata):
    from collections import defaultdict
    
    if not stdata:
        raise Exception("Empty input list")
    
    scores = defaultdict(int)
    for name, score in stdata:
        scores[name] += score
        
    max_student = max(scores, key=scores.get)
    return (max_student, scores[max_student])
import unittest

class Test(unittest.TestCase):
    def test_max_aggregate(self):
        self.assertEqual(max_aggregate([('Juan Whelan',90),('Sabah Colley',88),('Peter Nichols',7),('Juan Whelan',122),('Sabah Colley',84)]), ('Juan Whelan', 212))

if __name__ == '__main__':
    unittest.main()