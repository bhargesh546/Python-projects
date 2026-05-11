questions = ("Which animal lays the largest egg?",
             "What is the most abundant gas in Earth?",
             "How many bones are there in a human body?",
             "Which planet is the hottest in the solar system?")

options = (("A.", "B.", "C.", "D."), 
           ("A.", "B.", "C.", "D."), 
           ("A.", "B.", "C.", "D."), 
           ("A.", "B.", "C.", "D."))

answers = ("", "", "", "")

score = 0
guesses = []
question_num = 0

for question in questions:
    print(f"{"-"*30}")
    print(question)
    for option in options[question_num]:
        print(option)
    
    guess = input("Enter an option: ").upper()
    guesses.append(guess)

    if guess == answers[question_num]:
        score += 1
        print("Correct!")
    else:
        print("Incorrect!")
        print(f"The correct answer is: {answers[question_num]}")

    question_num += 1

print(f"Your total score is {score} ({score/len({questions}):.0%})")