def max_aggregate(stdata):
    # Write your code here
    max_aggregate = {}
    for name, value in stdata:
        if name in max_aggregate:
            max_aggregate[name] += value
        else:
            max_aggregate[name] = value

    max_name = max(max_aggregate, key=max_aggregate.get)
    return (max_name, max_aggregate[max_name])
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(max_aggregate([('Juan Whelan',90),('Sabah Colley',88),('Peter Nichols',7),('Juan Whelan',122),('Sabah Colley',84)]),('Juan Whelan', 212))

if __name__ == '__main__':
    unittest.main()