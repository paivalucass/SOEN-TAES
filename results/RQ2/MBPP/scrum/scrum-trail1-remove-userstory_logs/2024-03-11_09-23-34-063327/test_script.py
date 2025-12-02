def sum_list(lst1, lst2):
    if len(lst1) != len(lst2):
        return "Error: Input lists are of different lengths"
    
    summed_list = [x + y for x, y in zip(lst1, lst2)]
    return summed_list
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sum_list([10, 20, 30], [15, 25, 35]), [25, 45, 65])

if __name__ == '__main__':
    unittest.main()