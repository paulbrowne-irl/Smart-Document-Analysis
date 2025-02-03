import unittest
import shelve
import info.score
import extract.convert
import one_client_pdf

class Test_Convertor(unittest.TestCase):

    def test_generate_tmp_output_filename(self):
        tmp_name=extract.convert.generate_tmp_output_filename("somename.xls",one_client_pdf.tmp_dir)
        print(tmp_name)

    def test_word_convert(self):
        infile = str(one_client_pdf.header_template)
        tmp_name=extract.convert.convert_word_file_to_pdf(infile,"C:/tmp/"+ "test.pdf")
    
    def test_combine(self):
        extract.convert.combine_pdf_documents("C:/tmp/","C:/tmp/z_combo.pdf")
    

if __name__ == '__main__':
    unittest.main()
