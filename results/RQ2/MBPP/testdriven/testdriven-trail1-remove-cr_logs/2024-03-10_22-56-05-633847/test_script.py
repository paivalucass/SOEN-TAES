def Diff(li1, li2):
    diff_list = [item for item in li1 if item not in li2]
    diff_list.extend([item for item in li2 if item not in li1])
    return diff_list
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(Diff([10, 15, 20, 25, 30, 35, 40], [25, 40, 35]), [10, 20, 30, 15])

if __name__ == '__main__':
    unittest.main()