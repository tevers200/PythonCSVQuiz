from random import sample
from random import shuffle
import csv
import argparse
from colorama import Fore, Back, Style, init
import datetime
init(autoreset=True)

parser = argparse.ArgumentParser(description='Tamar\'s Python Quiz')
parser.add_argument('--number', metavar='N', type=int,
                    help='The number of questions to ask. Default 20.', default=20)
parser.add_argument('--file', default="questions.csv",
                    help='Default questions.csv. A CSV file containing questions in the format:\nQuestion,SyllabusArea,Advice,CorrectAnswer,WrongAnswer[n]...'),
parser.add_argument('-r', action='store_true', help='Prevent the questions from being asked in a random order (defaults to random if this flag is not set).')
parser.add_argument('-a', action='store_true', help='Hides the advice text shown after each question (shows the advice by default if this flag is not set).')
parser.add_argument('-s', action='store_true', help='Hides the score for each question (correct/incorrect) and only shows your overall score at the end of the quiz')
parser.add_argument('-t', action='store_true', help='Hides the time taken for the quiz, and average time per question (shows the timings by default if this flag is not set).')

args = parser.parse_args()


class Question:
    def __init__(self, prompt, answer, advice, syllabusArea):
        self.prompt = prompt
        self.correctAnswer = answer[0]
        self.answers = sample(answer, len(answer))
        self.advice = advice
        self.syllabusArea = syllabusArea


if args.file:
    quizfile = args.file
else:
    quizfile = "questions.csv"
if args.r:
    randomize = False
else:
    randomize = True
if args.a:
    advice = False
else:
    advice = True
if args.s:
    showscore = False
else:
    showscore = True
if args.t:
    time = False
else:
    time = True
numQuestions = int(args.number)

numbering = "abcdefghijklmnopqrstuvwxyz"



def load_quiz(quizfile,randomize):
    questions = []
    with open(quizfile) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                ans = []
                num = 0
                for item in row:
                    if num > 2:
                        ans.append(item)
                    num += 1

                q = {'question': row[0], 'syllabusArea': row[1], 'advice': row[2], 'answers': ans}
                questions.append(q)
                line_count += 1
    if randomize is True:
        shuffle(questions)
    return questions

def run_quiz(questions,numQuestions):
    starttime = datetime.datetime.now()
    score = 0
    qNum = 0
    if(numQuestions > len(questions)):
        total = len(questions)
    else:
        total = numQuestions
    if randomize:
        text = Style.BRIGHT + "random " + Style.RESET_ALL
    else:
        text = ""
    print(f'You will be asked {total} {text}questions out of the pool of {len(questions)}\n\n')
    for question in questions:
        if qNum < numQuestions:
            qNum += 1
            correct = 0
            print(Style.BRIGHT + f'Question {qNum}')
            print(f'\n{question.prompt}\n')
            i = 0
            for answer in question.answers:
                print(numbering[i] + ". " + answer, "\n")
                if answer == question.correctAnswer:
                    correct = i
                i += 1
            while True:
                answer = input().strip()
                if (len(answer) == 1) and answer in numbering[0:i]:
                    break
                else:
                    print(Fore.RED + "Invalid response. Try again.")
            if answer == numbering[correct]:
                if showscore:
                    print(Fore.GREEN + Style.BRIGHT + "\nCorrect\n")
                score += 1
            else:
                if showscore:
                    print(Fore.RED + Style.BRIGHT + f'\nIncorrect\n\n')
                    print(f'Correct Answer: \n{question.correctAnswer}\n')
            if advice:
                print(Fore.MAGENTA + Style.BRIGHT + f'\nAdditional Info:')
                print(f'Syllabus area: s{question.syllabusArea}\n')
                print(f'{question.advice}\n\n================================================\n\n')
        else:
            break
    totaltime = datetime.datetime.now() - starttime

    print("\n\nYou got", score, "out of", total)
    percentage = (score / total) * 100
    print(f'{percentage}%')
    print("\n\nThe quiz took you", totaltime, "to complete. The average time spent per question was", totaltime/total)


questions = load_quiz(quizfile, randomize)



qs = []
for question in questions:
    qs.append(Question(question["question"], question["answers"], question["advice"], question["syllabusArea"]))
run_quiz(qs,numQuestions)