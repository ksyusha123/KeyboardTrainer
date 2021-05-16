import unittest
import statistics


class Test(unittest.TestCase):
    def test_accuracy(self):
        self.assertEqual(100, statistics.get_accuracy(10, 0))
        self.assertEqual(50, statistics.get_accuracy(8, 4))
        self.assertEqual(0, statistics.get_accuracy(10, 10))
        self.assertEqual(0, statistics.get_accuracy(0, 0))

    def test_speed(self):
        self.assertEqual(400, statistics.get_speed(20, 3))
        self.assertEqual(0, statistics.get_speed(0, 3))

    def test_instantaneous_speed(self):
        self.assertEqual(400, statistics.get_instantaneous_speed(20, 3))
        self.assertEqual(0, statistics.get_instantaneous_speed(0, 0))


if __name__ == '__main__':
    unittest.main()
