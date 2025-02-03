import unittest
import logging
import os

import pandas as pd

import testsettings

# allow imports from parent directory
import sys
sys.path.append('../project_xl')
import util.table_names as table_names
import collate

class Test_Collate_Table(unittest.TestCase):
   
    @classmethod
    def setUpClass(self):
       
        #setup logging
        logger = logging.getLogger("..")
        logger.setLevel(logging.DEBUG)
    
    def test_get_skip_list(self):
        file_list=collate._get_skip_list()
        self.assertGreater(len(file_list),0)
        print(file_list)

''' 
    def test_rename(self):

        main_df = pd.DataFrame( columns=['small1', 'small2'])
        to_merge_df = pd.DataFrame()

        #We try this both ways around       
        outputdf1= collate._rename_columns(main_df)
        outputdf2= collate._rename_columns(to_merge_df)
    

    def test_remove_columns(self):
        
        main_df=pd.read_excel(testsettings.TEST_DF_CHECKLIST)
        
        collate._remove_duplicated_index_columns(main_df)

        self.assertEqual(len(main_df.columns),3)  # original dataset has 5 of which 2 removed
'''





unittest.main()

 