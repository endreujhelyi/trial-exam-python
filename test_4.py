import unittest
from task_4 import greeter

class TestGreeter(unittest.TestCase):

    def test_is_greeter_say_ya_name(self):
        self.assertEqual(greeter("Uncle Ben"), "Hello, Uncle Ben!")

    def test_is_greeter_knows_mr_nobody(self):
        self.assertEqual(greeter(""), "Hello, Mr Nobody!")

    def test_greeter_raise_typerror_if_get_int(self):
        self.assertRaises(TypeError, 4, greeter)



if __name__ == '__main__':
    unittest.main()
