# Python CSV Quiz
This is a Python3 quiz tool which reads in a CSV file of questions, randomizes the questions and answers, and then asks a set number of questions from the pool.

## Format for CSV Question Input File
There are four mandatory columns within the  CSV file:
* Questions
* Syllabus Area(s)
* Advice
* Correct answer  

You can then have as many wrong answers as you like after the correct answer, depending on the type of exam you are practicing for. I built this tool with CREST's CCT theory exam in mind, so usually have one correct answer and four incorrect answers for each question.  
A sample layout can be seen below:

| Questions   |      Syllabus Area(s)      |  Advice | Correct Answer | Wrong Answer N | Wrong Answer N+1 | Wrong Answer n+x
|----------|-------------|------|---|---|---|---|
| How many sides does a square have? |  A | Squares are made up of four equal-length sides | 4 | 1 | 2 |3 |
| Which of the following is NOT a valid DNS record type? |    A | News Server is not a valid DNS record type. | NWS - News Server   |   SOA - Start of Authority | CNAME - Canonical Name | MX - Mail eXchange |

## Usage
Currently, there are only three arguments, and these are all optional:

~~~~
usage: main.py [-h] [--number N] [--file FILE] [-r]

Tamar's Python Quiz

optional arguments:  
  -h, --help   show this help message and exit  
  --number N   The number of questions to ask. Default 20.  
  --file FILE  Default questions.csv. A CSV file containing questions in the
               format: Question,SyllabusArea,Advice,CorrectAnswer,WrongAnswer[n]...  
  -r           Prevent the questions from being asked in a random order
               (defaults to random if this flag is not set).  
~~~~

* --number  
The `--number` flag specifies how many questions to ask in the quiz. If this is greater than the total number of questions available in the CSV file, then the total number of available questions will be asked instead. If this flag is not set, 20 questions are asked by default.  
* --file  
The `--file` flag is used to pass a CSV file to the application which contains the questions. If no file is specified, the application will look for the file questions.csv in the current directory.  
* -r  
The `-r` flag takes no parameters. If it is specified, the questions will *NOT* be asked in a random order, and will instead be taken from the imported CSV, starting at the first line and working down until the total number of questions has been asked. Note that the answers will still be presented in a random order, however.

## Dependencies
The following dependencies must be installed in order for the quiz to run:
* Colorama (pip install colorama)

## Supported Platforms
The quiz has been tested and works on the following platforms. However, it should work on any platform which runs Python3.
* Windows 10
* Linux Mint
* Android

## Future Additions  
Currently, I have developed this quiz tool to the bare minimum needed to help me practice for my upcoming CCT exam. It would have been far too easy to continue adding features, but that would have eaten into the time I actually spent studying. As such, the below are features that I would like to add in but have not yet done:
* Make the Advice optional. Currently, advice is shown after every question is answered to provide additional information on the subject within the question. I have found this really useful as a learning aid, but the real exam doesn't give this advice! #2
* Allow the questions asked to be specified by syllabus level. E.g. within CREST's syllabus, section "E" relates to Microsoft Windows Security Assessment. If this was one of my weaker areas, I may want to quiz myself only on questions within this syllabus area. Likewise, I may want to exclude certain areas I'm very confident on. #6
* Hide the scoring for each question. Again, in the real exam you don't know your score until the end. It would be good to have the option to only show the results at the very end of the quiz. #3
* Show a score breakdown based on syllabus area. If I do really well on questions from Syllabus area "A", but really badly on syllabus area "B", I want to know so that I can focus on the weaker areas. #5
* Provide a runtime flag which allows the time taken to be tracked (show the start time at the beginning, and the end time and total time at the end) #4
