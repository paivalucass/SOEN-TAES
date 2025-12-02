def divisible_by_digits(startnum, endnum):
    '''
    Write a function to find numbers within a given range from startnum to endnum where every number is divisible by every digit it contains. https://www.w3resource.com/python-exercises/lambda/python-lambda-exercise-24.php
    assert divisible_by_digits(1,22)==[1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
    '''
    result = []
    for num in range(startnum, endnum+1):
        if num <= 0:
            continue
        num_str = str(num)
        divisible = True
        for digit in num_str:
            if int(digit) == 0:
                divisible = False
                break
            if num % int(digit) != 0:
                divisible = False
                break
        if divisible:
            result.append(num)
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(divisible_by_digits(1, 22), [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22])

if __name__ == '__main__':
    unittest.main()