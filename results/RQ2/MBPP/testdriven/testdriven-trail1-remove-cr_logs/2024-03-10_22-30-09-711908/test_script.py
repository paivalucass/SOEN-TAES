def frequency_lists(list1):
    try:
        if not isinstance(list1, list):
            raise TypeError("Input should be a list of lists")
        
        flattened_list = [item for sublist in list1 for item in sublist]
        
        if not flattened_list:
            raise ValueError("Input list is empty")
        
        for sublist in list1:
            for element in sublist:
                if not isinstance(element, (int, float, str)):
                    raise TypeError("Elements within the lists are not hashable")
        
        frequency_dict = {}
        for element in flattened_list:
            frequency_dict[element] = frequency_dict.get(element, 0) + 1
        
        return frequency_dict
    except Exception as e:
        return f"Error: {str(e)}"
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(frequency_lists([[1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5]]), {1: 1, 2: 3, 3: 1, 4: 1, 5: 2, 6: 1, 7: 1, 8: 1, 9: 1})

if __name__ == '__main__':
    unittest.main()