import unittest
import shelve
import info.score


class Test_Quadrant_score(unittest.TestCase):

    def test_score_engagement(self):

        days_since = [29.39861111111111,
                      29.400694444444444,
                      46.111805555555556,
                      87.9986111111111,
                      51.98472222222222,
                      36.606944444444444,
                      88.30208333333334,
                      46.326388888888886,
                      52.08125,
                      29.400694444444444,
                      29.396527777777777,
                      29.4]

        score = info.score.score_engagement(days_since)
        print ("Test Score:"+str(score))

    def test_rebase_one_hundred(self):
    
        days_since = [29.39861111111111,
                      29.400694444444444,
                      46.111805555555556,
                      87.9986111111111,
                      51.98472222222222,
                      36.606944444444444,
                      88.30208333333334,
                      46.326388888888886,
                      52.08125,
                      29.400694444444444,
                      29.396527777777777,
                      29.4]

        score_list = info.score.rebase_list_one_hundred(days_since)
        print ("Test Score:"+str(score_list))

if __name__ == '__main__':
    unittest.main()
