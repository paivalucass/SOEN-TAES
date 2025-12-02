def merge_dictionaries_three(dict1, dict2, dict3):
    try:
        # Input validation to ensure all inputs are dictionaries
        if not isinstance(dict1, dict) or not isinstance(dict2, dict) or not isinstance(dict3, dict):
            raise ValueError("All inputs must be dictionaries")

        merged_dict = {}
        for d in [dict1, dict2, dict3]:
            merged_dict.update(d)

        return merged_dict
    except (AttributeError, TypeError):
        raise ValueError("Invalid input types")
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(merge_dictionaries_three({ "R": "Red", "B": "Black", "P": "Pink" }, { "G": "Green", "W": "White" },{ "O": "Orange", "W": "White", "B": "Black" }), {'B': 'Black', 'R': 'Red', 'P': 'Pink', 'G': 'Green', 'W': 'White', 'O': 'Orange'})

if __name__ == '__main__':
    unittest.main()