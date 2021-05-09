import unittest
import statistics


class Test(unittest.TestCase):
    def test_accuracy(self):
        self.assertEqual(100, statistics.get_accuracy('someText', 8))
        self.assertEqual(50, statistics.get_accuracy('someText', 4))
        self.assertEqual(0, statistics.get_accuracy('', 0))

    def test_right_symbols_amount(self):
        training_text = 'someText'
        self.assertEqual(
            8, statistics.get_right_symbols_amount('someText', training_text))
        self.assertEqual(
            7, statistics.get_right_symbols_amount('someTexg', training_text))
        self.assertEqual(
            7, statistics.get_right_symbols_amount('sometext', training_text))
        self.assertEqual(
            0, statistics.get_right_symbols_amount('', training_text))
        self.assertEqual(
            0, statistics.get_right_symbols_amount('', ''))


if __name__ == '__main__':
    unittest.main()
