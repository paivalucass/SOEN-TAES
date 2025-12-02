def common_element(list1, list2):
    try:
        if not list1 or not list2:
            raise ValueError("Input lists cannot be empty")
        
        common_elements = any(item in list1 for item in list2)
        return common_elements
    except Exception as e:
        print("An error occurred:", e)
import unittest

class Test(unittest.TestCase):
    def test_common_element(self):
        self.assertEqual(common_element([1,2,3,4,5], [5,6,7,8,9]), True)

if __name__ == '__main__':
    unittest.main()