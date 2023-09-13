import unittest
import test_subject

class TestMain(unittest.TestCase):
    def setUp(self):
        print("about to test a function")

    def test_do_stuff_success(self):
        '''
        INFO: Test for success case 
        '''
        test_param = 10
        result = test_subject.do_stuff(test_param)
        self.assertEqual(result, 15)
    
    def test_do_stuff_string_type(self):
        '''
        INFO: Test for string type
        '''
        test_param = 'blahblahblah'
        result = test_subject.do_stuff(test_param)
        self.assertIsInstance(result, ValueError)

    def test_do_stuff_none_type(self):
        '''
        INFO: Test for none type
        '''
        test_param = None
        result = test_subject.do_stuff(test_param)
        self.assertEqual(result, "Please enter number")

    def test_do_stuff_empty_string(self):
        '''
        INFO: Test for empty string
        '''
        test_param = ''
        result = test_subject.do_stuff(test_param)
        self.assertEqual(result, "Please enter number")

    def tearDown(self):
        print("cleaning up...")

if __name__ == "__main__":
    unittest.main()

