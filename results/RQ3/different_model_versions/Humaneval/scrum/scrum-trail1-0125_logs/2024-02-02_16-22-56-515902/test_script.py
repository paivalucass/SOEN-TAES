def create_number_names_dictionary():
    return {
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine"
    }

def by_length(arr):
    sorted_arr = sorted([num for num in arr if 1 <= num <= 9])
    reversed_arr = sorted_arr[::-1]
    
    number_names = create_number_names_dictionary()
    
    names_arr = [number_names[num] for num in reversed_arr]
    
    return names_arr

# Test Cases:
{
    "test_cases": [
        {
            "Test Title": "Test for empty array",
            "Input Data": "arr=[]",
            "Expected Output": "[]"
        },
        {
            "Test Title": "Test for strange numbers",
            "Input Data": "arr=[1,-1,55]",
            "Expected Output": "['One']"
        },
        {
            "Test Title": "Test for valid input arrays",
            "Input Data": "arr=[2,1,1,4,5,8,2,3]",
            "Expected Output": "['Eight','Five','Four','Three','Two','Two','One','One']"
        },
        {
            "Test Title": "Test for null array",
            "Input Data": "arr=null",
            "Expected Output": "[]"
        },
        {
            "Test Title": "Test for duplicate elements",
            "Input Data": "arr=[2,2,3,3,4,5,5,8]",
            "Expected Output": "['Eight','Five','Four','Three','Three','Two','Two','Two']"
        }
    ]
}
import unittest

class Test(unittest.TestCase):
    def test_by_length(self):
        self.assertEqual(by_length([2, 1, 1, 4, 5, 8, 2, 3]), ["Eight", "Five", "Four", "Three", "Two", "Two", "One", "One"])
        self.assertEqual(by_length([]), [])
        self.assertEqual(by_length([1, -1, 55]), ["One"])

if __name__ == '__main__':
    unittest.main()