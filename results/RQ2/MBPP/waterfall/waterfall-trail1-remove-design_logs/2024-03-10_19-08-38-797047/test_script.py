def frequency(a, x):
    frequency_map = {}
    for num in a:
        if num in frequency_map:
            frequency_map[num] += 1
        else:
            frequency_map[num] = 1
    return frequency_map.get(x, 0)
import unittest

class Test(unittest.TestCase):
    def test_frequency(self):
        self.assertEqual(frequency([1,2,3], 4), 0)

if __name__ == '__main__':
    unittest.main()