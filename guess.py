import random

max_try = 0;
target = random.randint(1,20)

#print(target);


while(max_try < 6):
    print('Please enter your guess: ')
    myguess = int(input())
    
    max_try += 1
    
    if myguess == target:
        print('You have guessed it right')
        break;
    
    if myguess > target:
        print('Your guess is too high')
        
    if myguess < target:
        print('Your guess is too low')
    
print(' \n You have exhausted all your tries, the target was {}'.format(target))
