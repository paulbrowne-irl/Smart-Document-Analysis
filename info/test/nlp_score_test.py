import unittest
import shelve

from dominate.tags import p

import info.nlp_score


class Test_NLP_Score(unittest.TestCase):

    def test_nlp_scoring(self):
        score = info.nlp_score.nlp_score_file("test_data/simple.docx")
        print (f"test score:{score}")

if __name__ == '__main__':
    unittest.main()