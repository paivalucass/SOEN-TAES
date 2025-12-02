def mul_even_odd(list1):
    if len(list1) == 0:
        return "Error - Input list is empty. Program should return an error message"

    even_found = False
    odd_found = False
    product = 1

    for num in list1:
        if not isinstance(num, (int, float)):
            return "Error - Input list contains non-numeric values"

        if num % 2 == 0 and not even_found:
            product *= num
            even_found = True
        elif num % 2 != 0 and not odd_found:
            product *= num
            odd_found = True

        if even_found and odd_found:
            break

    if not even_found or not odd_found:
        if even_found:
            return "Error - No odd number in the list. Program should return an error message"
        elif odd_found:
            return "Error - No even number in the list. Program should return an error message"

    return product

# Test cases
assert mul_even_odd([]) == "Error - Input list is empty. Program should return an error message"
assert mul_even_odd([2,4,6,8]) == "Error - No odd number in the list. Program should return an error message"
assert mul_even_odd([1,3,5,7]) == "Error - No even number in the list. Program should return an error message"
assert mul_even_odd([1,2,3,4,5,6,7]) == 2
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(mul_even_odd([1,3,5,7,4,1,6,8]), 4)

if __name__ == '__main__':
    unittest.main()