def overlapping(list1, list2):
    if not isinstance(list1, list) or not isinstance(list2, list):
        raise TypeError("Input parameters list1 and list2 should be lists")

    set_list2 = set(list2)
    for val in list1:
        if val in set_list2:
            return True
    return False

# Test Cases:
assert overlapping([],[]) == False
assert overlapping([1],[6,7,8,9]) == False
assert overlapping([1,2,3,4,5],[3,4,5,6]) == True
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(overlapping([1,2,3,4,5],[6,7,8,9]), False)

if __name__ == '__main__':
    unittest.main()