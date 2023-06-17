from gpt_number import ai
from gpt_number_unProbable import ai_n
from firstNumber import first_list, last_win, duplicates, array
from getFile import getFiles
import unittest
import random as r
from em import sendEmail

mm_file = 'mm.csv'
pb_file = 'pb.csv'

getFiles()
def luckyPrint():
    first = sorted(first_list)
    second = sorted(r.sample(range(1, 70), 5)) + r.sample(range(1, 25), 1)
    third = []
    fourth = []
    mm = last_win(mm_file)
    pb = last_win(pb_file)
    golden = (1 + 5 ** 0.5) / 2
    # golden = (1 + 5 ** 0.5) / 2
    for i in range(6):
        third.append(duplicates(array(mm_file, i + 1), "max"))
        fourth.append(duplicates(array(pb_file, i + 1), "max"))
    html = '''<html><body><p>Hi, I have the following numbers for you!</p>
            <p>Golden ratio is: 
            </p>''' + str(first) + '''</p>
            <p>"================="</p>
            <p>1: ''' + str(first) + '''</p>
            <p>2: ''' + str(second) + '''</p>
            <p>MM: ''' + str(third) + '''</p>
            <p>PB: ''' + str(fourth) + '''</p>
            <p>"=========GPT========"</p>
            <p>MM_ai: ''' + str(ai('mm.csv')) + '''</p>
            <p>PB_ai: ''' + str(ai('pb.csv')) + '''</p>
             <p>"=========GPT====noProb===="</p>
            <p>MM_ai: ''' + str(ai_n('mm.csv')) + '''</p>
            <p>PB_ai: ''' + str(ai_n('pb.csv')) + '''</p>
            <p>"=======WON=========="</p>
            <p>MM last won is: 
            </p>''' + str(mm) + '''</p>
            <p>PB last won is: 
            </p>''' + str(pb) + '''</p>
            </body></html>'''
    return html


if __name__ == '__main__':
    sendEmail(luckyPrint())
    print(luckyPrint())
    unittest.main()