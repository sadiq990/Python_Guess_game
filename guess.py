# this is our secret text
secret_word = ("Lion")
guess = ("")
guess_count = 0
guess_limit = 3
out_of_guess = False

while guess != secret_word and not(out_of_guess):
    if guess_count < guess_limit:
       guess = input("Enter guess: ")
       guess_count += 1
    else:
       out_of_guess = True

if out_of_guess:
    print("you lose")
else:
    print("you win")
    
