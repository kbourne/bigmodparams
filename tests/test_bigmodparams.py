import unittest
from bigmodparams import example_function

class TestBigModParams(unittest.TestCase):
    def test_example_function(self):
        self.assertEqual(example_function(), "Hello from bigmodparams!")

if __name__ == '__main__':
    unittest.main()