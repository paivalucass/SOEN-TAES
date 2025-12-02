def merge_dictionaries_three(dict1, dict2, dict3):
    if not all(isinstance(d, dict) for d in [dict1, dict2, dict3]):
        raise ValueError("All input parameters must be dictionaries")

    merged = {}
    for d in [dict1, dict2, dict3]:
        for key, value in d.items():
            merged[key] = value
    return merged
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(merge_dictionaries_three({ "R": "Red", "B": "Black", "P": "Pink" }, { "G": "Green", "W": "White" },{ "O": "Orange", "W": "White", "B": "Black" }), {'R': 'Red', 'B': 'Black', 'P': 'Pink', 'G': 'Green', 'W': 'White', 'O': 'Orange'})

if __name__ == '__main__':
    unittest.main()