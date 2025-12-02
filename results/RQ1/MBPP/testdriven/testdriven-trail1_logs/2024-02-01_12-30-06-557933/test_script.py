def max_aggregate(stdata):
    max_aggregate = {}
    for name, score in stdata:
        if name in max_aggregate:
            max_aggregate[name] += score
        else:
            max_aggregate[name] = score

    max_student = max(max_aggregate, key=max_aggregate.get)
    return (max_student, max_aggregate[max_student])
import unittest

class Test(unittest.TestCase):
    def test_max_aggregate(self):
        self.assertEqual(max_aggregate([('Juan Whelan',90),('Sabah Colley',88),('Peter Nichols',7),('Juan Whelan',122),('Sabah Colley',84)]), ('Juan Whelan', 212))

if __name__ == '__main__':
    unittest.main()