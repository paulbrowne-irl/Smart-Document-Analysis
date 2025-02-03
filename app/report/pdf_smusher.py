'''
Tools to combine documents into one PDF
'''

import extract.convert

def generate_front_page(front_page_template,pdf_output_file):
    ''' 
    Generate our Front page template
    :param front_page_template - path to where template sits
    :param pdf_outputfile - name (not path) that we will call this pdf
    '''

    extract.convert.convert_word_file_to_pdf(front_page_template,pdf_output_file)
    print("Converted front page to:"+output_name)