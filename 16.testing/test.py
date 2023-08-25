import unittest

from main import do_stuff

class TestMain(unittest.TestCase):
    def test_do_stuff(self):
        num = 10 # random number
        result = do_stuff(num)
        # here is the keypart
        self.assertEqual(result, 15) # assertequal build in from inheritance unit test, assert equal check equality in 2 params
    # bellow is the next testing of the same function
    def test_do_stuff2(self):
        num = 'sssss' # random number
        result = do_stuff(num)
        # here is the keypart
        self.assertIsInstance(result,ValueError)
unittest.main()