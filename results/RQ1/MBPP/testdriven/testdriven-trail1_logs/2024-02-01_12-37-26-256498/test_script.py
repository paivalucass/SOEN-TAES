def rearrange_bigger(n):
    '''Write a function to create the next bigger number by rearranging the digits of a given number.'''
    if not isinstance(n, int):
        raise ValueError("Invalid input")
    if n < 0:
        raise ValueError("Negative number not allowed")
    digits = [int(d) for d in str(n)]
    pivot = find_pivot(digits)
    if pivot == -1:
        return "No bigger number can be formed"
    next_smallest = find_next_smallest(digits, pivot)
    digits[pivot], digits[next_smallest] = digits[next_smallest], digits[pivot]
    result = int("".join(map(str, digits[:pivot + 1] + sorted(digits[pivot + 1:])))
    return result

def find_pivot(digits):
    for i in range(len(digits) - 1, 0, -1):
        if digits[i] > digits[i - 1]:
            return i - 1
    return -1

def find_next_smallest(digits, pivot):
    next_smallest = min([x for x in digits[pivot+1:] if x > digits[pivot]])
    return pivot + 1 + digits[pivot+1:].index(next_smallest)

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(rearrange_bigger(12), 21)

if __name__ == '__main__':
    unittest.main()