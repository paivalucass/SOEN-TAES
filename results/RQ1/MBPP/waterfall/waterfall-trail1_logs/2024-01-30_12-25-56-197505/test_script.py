def merge_dictionaries_three(dict1, dict2, dict3):
    all_keys = set(dict1.keys()).union(set(dict2.keys()), set(dict3.keys()))
    if len(all_keys) != len(dict1) + len(dict2) + len(dict3):
        raise ValueError("Input dictionaries have overlapping keys")
    
    merged_dict = dict1.copy()
    for d in [dict2, dict3]:
        for k,v in d.items():
            if k in merged_dict:
                raise ValueError("Input dictionaries have overlapping keys")
            merged_dict[k] = v
    
    return merged_dict
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(merge_dictionaries_three({ "R": "Red", "B": "Black", "P": "Pink" }, { "G": "Green", "W": "White" },{ "O": "Orange", "W": "White", "B": "Black" }), {'B': 'Black', 'R': 'Red', 'P': 'Pink', 'G': 'Green', 'W': 'White', 'O': 'Orange'})

if __name__ == '__main__':
    unittest.main()