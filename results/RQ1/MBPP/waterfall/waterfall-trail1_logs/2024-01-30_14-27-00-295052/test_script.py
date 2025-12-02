def common_element(list1, list2):
    if not isinstance(list1, list) or not isinstance(list2, list):
        raise ValueError("Input parameters must be lists")

    for element in list1:
        if not isinstance(element, int):
            raise ValueError("List must contain only integers")

    for element in list2:
        if not isinstance(element, int):
            raise ValueError("List must contain only integers")

    for element in list1:
        if element in list2:
            return True

    return False
import unittest

class Test(unittest.TestCase):
    def test_common_element(self):
        self.assertEqual(common_element([1,2,3,4,5], [5,6,7,8,9]), True)

if __name__ == '__main__':
    unittest.main()