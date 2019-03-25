'''
Created on Jan 4, 2019

@author: vkhoday
'''
import HtmlTestRunner
import unittest
import logging

list_lst =['a','b','c','d']
class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

#     def test_error(self):
#         """ This test should be marked as error one. """
#         raise ValueError

    def test_fail(self):
        """ This test should fail. """
        for j in list_lst:
            print (logging.info(j))
        self.assertEqual(1, 1)

    @unittest.skip("This is a skipped test.")
    def test_skip(self):
        """ This test should be skipped. """
        
#         HtmlTestRunner.result.TestResult.addSuccess(self, Test_1)
        pass

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='example_dir'))
    for j in list_lst:
        print (logging.info(j))
