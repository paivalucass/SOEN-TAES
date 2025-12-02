def sort_numeric_strings(nums_str):
    try:
        if all(num_str.lstrip('-').replace('.','',1).isdigit() for num_str in nums_str):
            return sorted(nums_str, key=lambda x: int(x))
        else:
            return "Error: Input must be a list of strings containing only numeric values"
    except Exception as e:
        return f"Error: {e}"
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sort_numeric_strings(['4','12','45','7','0','100','200','-12','-500']), [-500, -12, 0, 4, 7, 12, 45, 100, 200])

if __name__ == '__main__':
    unittest.main()