import pandas as pd
import pprint
import qnas
import random

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def parse_qna():

    qnas = []

    is_new = True

    with open('qna.csv', 'r', encoding='utf-8') as file:
        for line in file.readlines():

            line.strip()
            line = line[:-1]

            if is_new:
                is_new = False
                qna = dict()
                qna['question'] = line
                qna['anwsers'] = []
                qna['correct'] = 9
                qnas.append(qna)
            elif line:
                is_new = False
                qnas[-1]['anwsers'].append(line)
            else:
                is_new = True

    with open('output.txt', 'wt', encoding='utf-8') as out:
        pprint.pprint(qnas, stream=out)


if __name__ == "__main__":
    n_questions = 10

    tmp = [ qna for qna in qnas.qnas if qna['correct'] != 9 ]
    sampled_qnas = random.sample(tmp, n_questions)
    print('Total number of questions: %d' % len(tmp))

    abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

    letter_to_number = {
        'a': 0,
        'b': 1,
        'c': 2,
        'd': 3,
        'e': 4,
        'f': 5,
        'g': 6,
    }

    number_to_letter = {
        0: 'a',
        1: 'b',
        2: 'c',
        3: 'd',
        4: 'e',
        5: 'f',
        6: 'g',
    }

    n_correct = 0

    for i,random_qna in enumerate(sampled_qnas):
        print('%d. %s' % (i+1, random_qna['question']))

        shuffled_anwsers = list(zip(range(10), random_qna['anwsers']))
        random.shuffle(shuffled_anwsers)

        for j, (index, anwser) in enumerate(shuffled_anwsers):
            print('  %s) %s' % (abc[j], anwser))

        user_input = input("Correct anwser: ")

        if shuffled_anwsers[letter_to_number[user_input]][0] == random_qna['correct']:
            print('%sYou are correct!%s\n' % (bcolors.OKGREEN, bcolors.ENDC))
            n_correct += 1
        else:
            correct_index = [ ind for ind, anw in shuffled_anwsers ].index(random_qna['correct'])
            print('%sCorrect anwser was %s).%s\n' % (bcolors.WARNING, number_to_letter[correct_index], bcolors.ENDC))

    print('FINAL SCORE: %d' % (n_correct/n_questions * 100))
