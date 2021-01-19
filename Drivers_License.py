# Text file opens for writing of student/user inputs
# List of correct answers' length is generated
# User enters A,B,C,D for all 20 questions
# Entries are recorded in .txt file with new line
# .txt file is closed to end function
def storeToFile(studentAnswers, correctAnswers):
    studentFile = open(studentAnswers, "w")
    numberQuestions = len(correctAnswers)
    
    for userAnswerIndex in range(numberQuestions):
        userAnswer = input("Please enter the answer for question " + \
                          str((userAnswerIndex + 1)) + ": ")
        
        studentFile.write(userAnswer.upper() + "\n") 
    
    studentFile.close()

# Earlier .txt file opened and read onto empty list
# Line of text (hopefully A,B,C,D) is added and newline character is ignored
# 'studentAnswer' list generated for cross-reference
def studentAnswersToList(studentAnswers):
    studentAnswersList = []
    studentFile = open(studentAnswers, "r")
    
    for studentAnswer in studentFile:
        studentAnswer = studentAnswer.rstrip("\n")
        studentAnswersList.append(studentAnswer)
    
    return studentAnswersList

# Exam answers and student answers are arguments
# Tally of correct answeres is initialized
# Length of exam list is used to gauge
# 'examQuestionIndex' used to compare student input from correct record
# For each correct student answer, a tally is made until a sum total
def findNumberCorrect(examAnswersList, studentAnswersList):
    correctAnswers = 0
    numberQuestions = len(examAnswersList)
    
    for examQuestionIndex in range(numberQuestions):
        if studentAnswersList[examQuestionIndex] == \
           examAnswersList[examQuestionIndex]:
            correctAnswers = correctAnswers + 1
         
    return correctAnswers

# Difference in lengths between exam and correct quickly creates number wrong
def findNumberIncorrect(numberCorrect, numberQuestions):
    numberIncorrect = numberQuestions - numberCorrect   
    return numberIncorrect

# Same principle as applied before comparing student input and exam record
# For every mis-match, the index of that is recorded to the incorrects list
# Incorrect numbers list is generated of questions user got wrong on exam
def getIncorrectNumbers(examAnswersList, studentAnswersList):
    incorrectNumbersList = []
    numberQuestions = len(examAnswersList)
    
    for examQuestionIndex in range(numberQuestions):
        if studentAnswersList[examQuestionIndex] != \
           examAnswersList[examQuestionIndex]:
             incorrectNumbersList.append(examQuestionIndex + 1)
    
    return incorrectNumbersList

# Pass mark of 15 is compared to number of correct tally from student's input
# This controls pass/fail messaging at end of program
def studentPass(passMark, numberCorrect):
    if numberCorrect >= passMark:
        return True
    else:
        return False

# If there are incorrect results, the list of those index values is printed
# Otherwise, a message of all-correct is displayed
def printIncorrectList(incorrectNumbers):
      if len(incorrectNumbers) >= 1:  
        print("\n\nIncorrect Questions: ")
        for questionIndex in range(len(incorrectNumbers[0:-1])):
            print(incorrectNumbers[questionIndex], end = ", ")
        print("and " + str(incorrectNumbers[-1]) + ".")
      else:
        print("\n\nStudent answered all questions correctly.")

# The number of correct and incorrect are displayed
# Incorrect number list is also displayed
def printResults(numberCorrect, numberIncorrect, incorrectNumbersList):
    
    print("\n\n\nNumber of correctly answered questions: " + \
          str(numberCorrect), \
          "Number of incorrectly answered questions: " + \
          str(numberIncorrect), sep = "\n")
    
    print()
    printIncorrectList(incorrectNumbersList)

# Main function has correct numbers list to compare
# File name for program is stored here, as is the pass-mark requirement value
# Number of correct, incorrect are found from arguments from function values
# Pass/fail messaging is displayed from earlier function
def main():
    correctAnswersList = [ "A", "C", "A", "A", "D", "B", "C", "A", "C", "B", \
                           "A", "D", "C", "A", "D", "C", "B", "B", "D", "A" ]
 
    NUMBER_OF_QUESTIONS = len(correctAnswersList)
    FILE_NAME = "studentAnswers.txt"
    PASS_MARK = 15
    
    storeToFile(FILE_NAME, correctAnswersList)
    
    studentAnswersList = studentAnswersToList(FILE_NAME)
    
    numberCorrect = \
        findNumberCorrect(correctAnswersList, studentAnswersList)
    
    numberIncorrect = \
        findNumberIncorrect(numberCorrect, NUMBER_OF_QUESTIONS)
    
    incorrectNumbersList = \
        getIncorrectNumbers(correctAnswersList, studentAnswersList)
        
    printResults(numberCorrect, numberIncorrect, incorrectNumbersList)

    print()
        
    if studentPass(PASS_MARK, numberCorrect):
       print("\n\nThe student passed the exam.\n\n")
    else:
       print("\n\nThe student failed the exam.\n\n")
       
main()