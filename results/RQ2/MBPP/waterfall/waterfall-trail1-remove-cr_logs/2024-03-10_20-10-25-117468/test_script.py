def split_Arr(l, n):
    # Split the list at the nth element and add the first part to the end
    first_part = l[:n]
    second_part = l[n:]
    rearranged_list = second_part + first_part
    return rearranged_list
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(split_Arr([12,10,5,6,52,36], 2), [5,6,52,36,12,10])

if __name__ == '__main__':
    unittest.main()