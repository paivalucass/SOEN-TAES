def sort_counter(dict1):
    if not isinstance(dict1, dict) or not dict1:
        return "Invalid input"
    
    for key, value in dict1.items():
        if not isinstance(value, int):
            return "Invalid input"

    sorted_dict = sorted(dict1.items(), key=lambda x: x[1], reverse=True)
    return sorted_dict
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sort_counter({'Math':81, 'Physics':83, 'Chemistry':87}), [('Chemistry', 87), ('Physics', 83), ('Math', 81)])

if __name__ == '__main__':
    unittest.main()