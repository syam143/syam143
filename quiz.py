#__________________
def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 1
    for key in questions:
        print("______________________")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("enter (a,b,or c): ")
        guess = guess.lower()
        guesses.append(guess)
        correct_guesses += check_answer(questions.get(key), guess)
        question_num +=1
    display_score(correct_guesses, guesses)
#______________________
def check_answer(answer, guess):
    if answer == guess:
        print("correct")
        return 1
    else:
        print("wrong")
        return 0
#_________________________
def display_score(correct_guess, guesses):
    print("__________________")
    print('results')
    print("__________________")

    print("answers: ", end= " ")
    for i in questions:
        print(questions.get(i), end= " ")
    print()

    print("guesses: ", end=" ")
    for i in guesses:
        print(i, end = "")
    print()

    score = int((correct_guess/len(questions)*100))
    print("your score is : " +str(score)+ "%")
    #__________________________
def play_again():


    response = input("do you want to play again (yes/no): ")
    response = response.lower()

    if response == "yes":
        return True
    else:
        return False
#__________________________

questions = {
    "who created python?: ": "a",
    "what yesr was python created: ": "b",
    "python is tributed to which comedy?: ": "a",
    "is earth is round? :  ": "a"
}

options = [["a. gudio van rossam", "b. elon muck", "c. tesla"],
           ["a. 1989", "b. 1991", "c. 2000"],
           ["a. lonely", "b. smosh", "c. monty"],
           ["a. true", "b. false", "c. wat to guess"]]
new_game()
while play_again():
    new_game()
print("byeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee")