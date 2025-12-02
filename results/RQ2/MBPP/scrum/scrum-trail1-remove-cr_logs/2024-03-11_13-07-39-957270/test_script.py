def max_aggregate(stdata):
    name_aggregate = {}
    
    for name, value in stdata:
        if name in name_aggregate:
            name_aggregate[name] += value
        else:
            name_aggregate[name] = value
    
    max_name = max(name_aggregate, key=name_aggregate.get)
    max_aggregate = name_aggregate[max_name]
    
    return (max_name, max_aggregate)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(max_aggregate([('Juan Whelan',90),('Sabah Colley',88),('Peter Nichols',7),('Juan Whelan',122),('Sabah Colley',84)]), ('Juan Whelan', 212))

if __name__ == '__main__':
    unittest.main()