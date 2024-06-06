import random

u_w = 0
c_w = 0

o = ["rock", "paper", "scissors"]

while True:
    u_i = input("Choose Rock/Paper/Scissors or Q to quit: ").lower()
    if u_i == "q":
        break

    if u_i not in o:
        continue

    r_n = random.randint(0, 2)
    c_p = o[r_n]
    print("Computer chose", c_p + ".")

    if u_i == "rock" and c_p == "scissors":
        print("You win!")
        u_w += 1

    elif u_i == "paper" and c_p == "rock":
        print("You win!")
        u_w += 1

    elif u_i == "scissors" and c_p == "paper":
        print("You win!")
        u_w += 1

    else:
        print("You lose!")
        c_w += 1

print("You won", u_w, "times.")
print("The computer won", c_w, "times.")
print("Goodbye!")
