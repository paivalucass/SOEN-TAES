def centered_hexagonal_number(n):
    '''Write a function to find nth centered hexagonal number.'''
    
    # input validation
    if not isinstance(n, int) or n <= 0:
        return "Error: Input must be a positive integer"

    # calculate the centered hexagonal number
    return n * (2 * n - 1)

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(centered_hexagonal_number(10), 271)

if __name__ == '__main__':
    unittest.main()