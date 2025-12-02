def count_element_in_list(list1, x):
    try:
        if not isinstance(list1, list):
            raise ValueError("Input 'list1' should be a nested list")
        
        if not all(isinstance(sublist, list) for sublist in list1):
            raise ValueError("Input 'list1' should be a nested list")

        if not isinstance(x, int):
            raise ValueError("Input 'x' should be an integer")

        count = sum(1 for sublist in list1 if x in sublist)
        return count

    except Exception as e:
        print(f"Error: {e}")
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(count_element_in_list([[1, 3], [5, 7], [1, 11], [1, 15, 7]], 1), 3)

if __name__ == '__main__':
    unittest.main()