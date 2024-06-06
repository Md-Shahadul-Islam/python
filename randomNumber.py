import random

#only genarates number between 0 to 10
#r = random.randrange(11)
#print(r)
#only genarates number between -5 to 10
#R =random.randrange(-5,11)
#only genarates number between -5 to 11
#p =random.randint(-5 , 11)

import random

t_r = input("Enter a number: ")

if t_r.isdigit():
    t_r = int(t_r)

    if t_r <= 0:
        print('Please enter a number larger than 0 next time.')
        quit()
else:
    print('Please enter a number next time.')
    quit()

r_n = random.randint(0, t_r)
g = 0

while True:
    g += 1
    u_g = input("Take a guess: ")
    if u_g.isdigit():
        u_g = int(u_g)
    else:
        print('Please enter a number next time.')
        continue

    if u_g == r_n:
        print("Correct!")
        break
    elif u_g > r_n:
        print("Too high!")
    else:
        print("Too low!")

print("Correct in", g, "attempts")
