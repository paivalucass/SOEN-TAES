def find_remainder(arr, n):
    try:
        if arr is None or n == 0:
            return None  # handle edge cases

        product = 1
        for num in arr:
            if type(num) != int:
                return None  # handle non-integer values in array
            product *= num

        remainder = product % n
        return remainder

    except Exception as e:
        print(f"An error occurred: {e}")
        return None  # handle any potential exceptions
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_remainder([100, 10, 5, 25, 35, 14], 11), 9)

if __name__ == '__main__':
    unittest.main()