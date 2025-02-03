import unittest

import report.flatten
from data import client_dto
from pandas import DataFrame

class TestReport(unittest.TestCase):
    '''
   Example given 
    NAME, DAYS_SINCE_LAST_UPDATE,ENGAGEMENT_SCORE,FILES	
    Acme corp, [92.14, 92.14, 91.95],8.91,['file1','file2','file3']

    it would generate
    NAME, DAYS_SINCE_LAST_UPDATE,ENGAGEMENT_SCORE,FILES	
    Acme corp, 92.14,8.91,'file1'
    Acme corp, 92.14,8.91,'file2'
    Acme corp, 91.95,8.91,'file3'

    '''
    def setUp(self):

        #Our test data to be converted
        test_dto = client_dto.ClientData()
        test_dto.set_name("Acme Corp")
        test_dto.set_days_since_last_update([92.14,92.14,91.95])
        test_dto.set_engagement_score(8.91)
        test_dto.set_filenames(['file1','file2','file3'])

        self.test_data = test_dto

    '''
    TODO:
        *write code
        Python type hinting
        plumb into snapshot.py
    '''


    def test_conversion(self):

        self.assertIsNotNone(self.test_data)

        #try the conversation
        my_data_frame = report.flatten.convert_dto_to_dataframe(self.test_data)
        print(my_data_frame)
      
      
        self.assertIsNotNone(my_data_frame,"Expected Dataframe, returned None")
        self.assertIsInstance(my_data_frame,DataFrame)
        self.assertEqual(4,my_data_frame.size) # WIDTH
        self.assertEqual(3,my_data_frame["ENGAGEMENT_SCORE"].count())


      
        

 

    def x_test_exception_throw(self):
        self.fail("Expected Exception not thrown")    

    def x_test_exlusion_list(self):
        self.fail("test not implemented yet")   

if __name__ == '__main__':
    unittest.main()