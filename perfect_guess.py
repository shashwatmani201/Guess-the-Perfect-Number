import random

random_no = random.randint(1,100)
user_guess = -1
no_of_guesses = 1
while(user_guess != random_no):
    user_guess = int(input(f"That's your {no_of_guesses} attempt, \nEnter your no:"))
    if(user_guess > random_no):
        print(f"\nTry to guess LOWER NO.")
        no_of_guesses += 1
        
    elif(user_guess < random_no):
        no_of_guesses += 1
        print(f"\nTry to guess HIGHER NO.")
        
    else:
        no_of_guesses += 1
        print(f"""\nCongratulations! You have guessed the correct no. in {no_of_guesses} attempts.
              \nAnd the number is {random_no}\n""")
        
