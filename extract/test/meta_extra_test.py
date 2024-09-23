import unittest
import shelve
import pprint

from . import meta_extract

class Test_Meta(unittest.TestCase):


    def test_text_extract_excel(self):
        clients = meta_extract.gatherInformation("..","z_scripts")

        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint(clients)
            

if __name__ == '__main__':
    unittest.main()