print("Welcome to my knowledge quiz!")

playing = input("Do you want to play? (yes/no) ")

if playing.lower() not in ("yes", "y"):
    quit()

print("Okay! Let's play :)")

questions = {
    "What does CPU stand for? ": "central processing unit",
    "What does GPU stand for? ": "graphics processing unit",
    "What does RAM stand for? ": "random access memory",
    "What does PSU stand for? ": "power supply"
}

score = 0
for question, answer in questions.items():
    user_answer = input(question).lower()
    if user_answer == answer:
        print('Correct!')
        score += 1
    else:
        print("Incorrect!")

print(f"You got {score} questions correct!")
print(f"You got {(score / 4) * 100:.1f}%.")
