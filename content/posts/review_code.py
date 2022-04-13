from random import randint
import os
import requests
import json

def main_quiz():
    global correct
    global incorrect

    #Start game options
    amount = input("Enter amount of questions you would like 1-50: ")
    os.system('clear')
    dif = input("Enter difficulty: easy, medium, hard: ")
    os.system('clear')
    #Print categorys
    print("Random: 0")
    print("General Knowledge: 9")
    print("Entertainment Film: 11")
    print("Entertainment Music: 12")
    print("Entertainment TV: 14")
    print("Science and Nature: 17")
    print("Sports: 21")
    print("Georgphy: 22")
    print("History: 23")
    print("Celebrities: 26")
    print("Vehicles: 28")
    print("Science: Gadgets: 30")
    category = input("Enter category ID:")
    os.system('clear')
    random = False
    if category == 0:
        random = True
    # Score Variables
    correct = 0
    incorrect = 0

    # Get list of questions from API Database
    response = requests.get(f"https://opentdb.com/api.php?amount={amount}&category={category}&difficulty={dif}&type=multiple")
    if random:
        response = requests.get(f"https://opentdb.com/api.php?amount={amount}&difficulty={dif}&type=multiple")
    # Create a formated string of the Python JSON object
    jsonDatabase = json.dumps(response.json(), sort_keys=True, indent=4)
    # Convert to Python list
    questionArray = json.loads(jsonDatabase)
    # Create the array to store the questions in
    questions = []
    #Index of array search
    qIndex = 0
    # Randomize awnsers order and add letter for correct awnser

    for i in questionArray['results']:
        questionArray['results'][qIndex]['incorrect_answers'].append(questionArray['results'][qIndex]['correct_answer']) # Also add the correct_answer to the list
        temp_array = []
        used_before = []
        tempIndex = 0
        correct_awnser_letter = ""
        for i in questionArray['results'][qIndex]['incorrect_answers']:
            tempIndex = randint(0, 3)
            while tempIndex in used_before:
                tempIndex = randint(0, 3)
            used_before.append(tempIndex)

            temp_array.append(questionArray['results'][qIndex]['incorrect_answers'][tempIndex])
        # Get the correct awnser in letter form eg. A. B. C. D
        correct_awnser_index = questionArray['results'][qIndex]['incorrect_answers'].index(questionArray['results'][qIndex]['correct_answer'])
        if correct_awnser_index == 0:
            correct_awnser_letter = "a"
        elif correct_awnser_index == 1:
            correct_awnser_letter = "b"
        elif correct_awnser_index == 2:
            correct_awnser_letter = "c"
        elif correct_awnser_index == 3:
            correct_awnser_letter = "d"
        NEW_ARRAY = [questionArray['results'][qIndex]['question'], questionArray['results'][qIndex]['incorrect_answers'][0], questionArray['results'][qIndex]['incorrect_answers'][1], questionArray['results'][qIndex]['incorrect_answers'][2], questionArray['results'][qIndex]['incorrect_answers'][3], correct_awnser_letter, questionArray['results'][qIndex]['correct_answer']]
        questions.append(NEW_ARRAY)

        qIndex = qIndex + 1

    # Function to print everything
    def main_display(question, optionA, optionB, optionC, optionD, correctA, correctAFull):
        global correct
        global incorrect

        # Print Question
        print(question)

        # Print Possible Awnsers
        print(f"A. {optionA}")
        print(f"B. {optionB}")
        print(f"C. {optionC}")
        print(f"D. {optionD}")

        # Input from user for their guess
        userInput = input('What is your guess? A. B. C. D.: ')

        if userInput.lower() == correctA:
            print("")
            print("Correct")
            correct = correct + 1
            clear_c = input('') # Wait for user input before clearing console
            os.system('clear')
        else:
            print("")
            print("Incorrect")
            print("")
            print("The correct awnser was: " + correctAFull)
            incorrect = incorrect + 1
            clear_c = input ('')
            os.system('clear')

    # Reset qIndex to be reused
    qIndex = 0

    # Print the question in the array
    for i in questions:
        main_display(questions[qIndex][0], questions[qIndex][1], questions[qIndex][2], questions[qIndex][3], questions[qIndex][4], questions[qIndex][5], questions[qIndex][6])
        qIndex = qIndex + 1

    # Print final score
    print("Correct: " + str(correct))
    print("Incorrect: " + str(incorrect))
    clear_c = input ('')
    os.system('clear')

GAME_RUNNING = True
while GAME_RUNNING:
    main_quiz()
    PLAY_GAME = input("Would you like to play again? y/n: ")
    os.system('clear')
    if PLAY_GAME.lower() == "n":
        GAME_RUNNING = False
