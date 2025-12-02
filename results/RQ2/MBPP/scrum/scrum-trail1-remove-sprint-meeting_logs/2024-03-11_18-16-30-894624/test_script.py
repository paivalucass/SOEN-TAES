def merge_dictionaries_three(dict1, dict2, dict3):
    if not isinstance(dict1, dict) or not isinstance(dict2, dict) or not isinstance(dict3, dict):
        raise TypeError("Input parameters must be dictionaries")

    if not dict1 or not dict2 or not dict3:
        raise ValueError("Input dictionaries cannot be empty")

    merged_dict = dict(dict1)
    merged_dict.update(dict2)
    merged_dict.update(dict3)

    return merged_dict
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertDictEqual(merge_dictionaries_three({ "R": "Red", "B": "Black", "P": "Pink" }, { "G": "Green", "W": "White" },{ "O": "Orange", "W": "White", "B": "Black" }), {'B': 'Black', 'R': 'Red', 'P': 'Pink', 'G': 'Green', 'W': 'White', 'O': 'Orange'})

if __name__ == '__main__':
    unittest.main()