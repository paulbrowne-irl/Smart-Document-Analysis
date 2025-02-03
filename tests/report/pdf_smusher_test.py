import unittest

import extract
import one_client_pdf as ocp
import report.pdf_smusher


class TestReport(unittest.TestCase):

    def test_front_page_gen(self):

        output_name= extract.convert.generate_tmp_output_filename(ocp.header_template,ocp.tmp_dir)

        print (f"about the convert front page template: template {ocp.header_template}\n outputname {output_name}")
        report.pdf_smusher.generate_front_page(ocp.header_name_in_folder,output_name)
        

if __name__ == '__main__':
    unittest.main()