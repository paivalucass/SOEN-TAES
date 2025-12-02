import unittest
def split(word):
    if not isinstance(word, str) or word == "":
        raise ValueError("Input must be a non-empty string")

    return [char for char in word]

# Test report and suggestions have been considered and 'unittest' module has been properly imported and defined to resolve the NameError.
class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(split('python'), ['p','y','t','h','o','n'])

if __name__ == '__main__':
    unittest.main()