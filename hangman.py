import random

# Write your code here
print("""H A N G M A N\n""")
words=['python', 'java', 'kotlin', 'javascript']
answer = random.choice(words)
count = 0
hint = list("-" * len(answer))
used = list()
while True:
    print('Type "play" to play the game, "exit" to quit:')
    choice = input()
    if choice == "play":
        while count < 8:
            print()
            print("".join(hint))
            guess = input("Input a letter: ")
            if len(guess) != 1:
                print("You should input a single letter")
            elif not guess.islower():
                print("It is not an ASCII lowercase letter")
            elif guess in answer:
                if guess in used:
                    print("You already typed this letter")
                else:
                    for i in range(len(answer)):
                        if answer[i] == guess:
                            hint[i] = guess
                    used.append(guess)
            elif guess in used:
                print("You already typed this letter")
            else:
                print("No such letter in the word")
                used.append(guess)
                count += 1
            if answer == hint:
                print("You guessed the word!\nYou survived!")
                break 
        else:
            print("You are hanged!")
            print()
            break
    elif choice == "exit":
        break
            
