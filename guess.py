# Simple guessing game.
import random
import time

max_try = 0;
target = random.randint(1,20)

print(target);


while(max_try < 3):
    print('Please enter your guess: ')
    myguess = int(input())

    max_try += 1

    if myguess == target:
        print('Checking your guess ....')
        time.sleep(2);
        print('Congratulations !!! ....You have guessed it right')
        break;

    if myguess > target:
        print('Checking your guess ....')
        time.sleep(2);
        print('Your guess is too high')

    if myguess < target:
        print('Checking your guess ....')
        time.sleep(2);
        print('Your guess is too low')

if(max_try == 3):
    print('Let me see .... Hmmm ....')
    time.sleep(2);
    print(' \n Sorry, You have exhausted all your tries, the target was {}'.format(target))
else:
    time.sleep(1);
    print('You are a true champion !')
