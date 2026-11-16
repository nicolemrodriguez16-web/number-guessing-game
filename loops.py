import random

secret = random.randint(1, 10)
max_tries = 5
tries = 1
guess = int(input("guess my number (1-10): "))

while guess != secret:
    if tries == max_tries:
       print("out of tries! the number was" , secret)
       break
    if guess < secret:
        print("too low!")
    else:
        print ("too high!")
    tries += 1
    guess = int(input("guess my number (1-10): "))
if guess == secret:
    print("you got it in" , tries, "tries!")
