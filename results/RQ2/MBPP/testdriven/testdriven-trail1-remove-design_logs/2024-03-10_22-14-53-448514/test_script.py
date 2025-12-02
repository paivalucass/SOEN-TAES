def swap_List(input_list):
    # Swap the first and last element in the list
    return [input_list[-1]] + input_list[1:-1] + [input_list[0] ]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(swap_List([1,2,3]), [3,2,1])

if __name__ == '__main__':
    unittest.main()