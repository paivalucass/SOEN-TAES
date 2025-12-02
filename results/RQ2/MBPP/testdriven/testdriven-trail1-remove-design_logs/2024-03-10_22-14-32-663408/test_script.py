def div_list(nums1, nums2):
    '''
    Write a function to divide two lists element wise.
    assert div_list([4,5,6],[1, 2, 3])==[4.0,2.5,2.0]
    '''
    if len(nums1) != len(nums2):
        raise ValueError("Input lists must be of the same length")

    result = []
    try:
        for i in range(len(nums1)):
            if nums2[i] == 0:
                raise ZeroDivisionError("Cannot divide by zero")
            result.append(nums1[i] / nums2[i])
        return result
    except (IndexError, ZeroDivisionError) as e:
        raise ValueError("Handle gracefully or return an error") from e
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(div_list([4, 5, 6], [1, 2, 3]), [4.0, 2.5, 2.0])

if __name__ == '__main__':
    unittest.main()