import random

def get_guess():
    while True:
        try:
            return int(input("guess my number (1-10):"))
        except ValueError:
            print("please enter a whole number!")

secret = random.randint(1, 10)
max_tries = 5
tries = 1
guess = get_guess()

while guess != secret:
    if tries == max_tries:
       print("out of tries! the number was" , secret)
       break
    if guess < secret:
        print("too low!")
    else:
        print ("too high!")
    tries += 1
    guess = get_guess()

if guess == secret:
    print("you got it in" , tries, "tries!")

