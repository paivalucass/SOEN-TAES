def overlapping(list1: list, list2: list) -> bool:
    if not all(isinstance(lst, list) for lst in [list1, list2]):
        raise TypeError("Both inputs should be lists")

    return any(item in list1 for item in list2)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(overlapping([1,2,3,4,5],[6,7,8,9]), False)

if __name__ == '__main__':
    unittest.main()