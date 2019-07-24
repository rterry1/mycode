#!/usr/bin/env python3

round = 0                           # interger round initiated to 0
while(true):                        # sets up an inifinate loop condition
        round = round + 1           # increase the round counter
        print(('Finish the movie title, "Monty Python\'s The Life of ______"')
        answer = input()            # string answer collected from user
        if (answer == 'Brian'):     # logic to check is user gave correct answer
            print('Correct') 
            break                   # break statement escapes the while loop
        elif (round == 3):          #loginc to ensure round has not yet reached 3
            print('Sorry, the answer was Brian.')
            break                   # break statement escapes the while loop
        else:
            print('Sorry. Try again!')
