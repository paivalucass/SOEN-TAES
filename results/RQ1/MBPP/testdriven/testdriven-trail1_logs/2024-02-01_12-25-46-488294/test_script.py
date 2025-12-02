def dict_filter(input_dict, threshold, greater_than=True):
    '''Filter the input dictionary based on the threshold value.'''
    if not isinstance(input_dict, dict):
        raise ValueError("Input is not a dictionary")
    
    # Filtering logic
    filtered_dict = {}
    if greater_than:
        for key, value in input_dict.items():
            if value >= threshold:
                filtered_dict[key] = value
    else:
        for key, value in input_dict.items():
            if value <= threshold:
                filtered_dict[key] = value

    if not filtered_dict:
        raise ValueError("No entries matched the filter criteria")

    return filtered_dict
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(dict_filter({'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}, 170), {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Pierre Cox': 190})

if __name__ == '__main__':
    unittest.main()