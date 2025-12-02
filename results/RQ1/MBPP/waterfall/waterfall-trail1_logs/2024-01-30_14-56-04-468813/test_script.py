def is_nonagonal(n):
    nonagonal_cache = {}

    if not isinstance(n, int) or n <= 0:
        return "Error: Input must be a positive integer"

    if n in nonagonal_cache:
        return nonagonal_cache[n]

    nonagonal_number = n * (7 * n - 5) // 2

    nonagonal_cache[n] = nonagonal_number

    return nonagonal_number
class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_nonagonal(10), 325)

if __name__ == '__main__':
    unittest.main()