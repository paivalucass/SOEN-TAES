def is_Sub_Array(main_array, sub_array):
    if len(sub_array) == 0:
        return True
    if len(main_array) == 0:
        return False
    for i in range(len(main_array)):
        if main_array[i] == sub_array[0]:
            if main_array[i:i+len(sub_array)] == sub_array:
                return True
    return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_Sub_Array([1, 4, 3, 5], [1, 2]), False)

if __name__ == '__main__':
    unittest.main()