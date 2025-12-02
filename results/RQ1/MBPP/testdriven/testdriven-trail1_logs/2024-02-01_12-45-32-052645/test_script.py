def find_adverb_position(text):
    '''
    Write a function to find the first adverb and its position in a given sentence.
    :param text: The input text in which to find the adverb position
    :return: A tuple containing the position of the adverb in the sentence and the adverb itself
    '''
    words = text.split()
    for i, word in enumerate(words):
        if word.rstrip('?!.,;:').endswith('ly'):
            return (i, text.find(word), word.rstrip('?!.,;:'))
    return None
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_adverb_position("clearly!! we can see the sky"), (0, 7, 'clearly'))

if __name__ == '__main__':
    unittest.main()