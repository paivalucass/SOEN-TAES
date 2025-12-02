def find_char_long(text):
    if text is None or text == "":
        return set()

    words = set()
    for word in text.split():
        if len(word) >= 4:
            words.add(word.strip(".,?!"))

    return words
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(set(find_char_long('Please move back to stream')), set(['Please', 'move', 'back', 'stream']))

if __name__ == '__main__':
    unittest.main()