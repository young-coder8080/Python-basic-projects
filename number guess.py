import random


def START(n):
    p_nm = input('\nEnter player name: ')
    print('You have {} attempts and {} hints. \n'.format(max_attempt, max_hint))    
    
    def Hint():
        global guess
        
        if guess < num:
            print('Your last number {} was too low'.format(guess))
        
        if guess > num:
            print('Your last number {} was too high'.format(guess))

    def Attempt():
        attempt = 1
        op = 'y'
        global guess
        global hints
        
        
        while op == 'y':
            guess = int(input('Guess a number between 1 and {}: '.format(n)))
            
            if guess < 1 or guess > n:
                print('ERROR: Number not in range.')
                
            if guess != num:
                attempt += 1
                ans = input('Do you want a hint y/n: ')
                if ans == 'y':
                    hints += 1
                    if hints < max_hint:
                        Hint()
                    else:
                        print('You have used all hints')
            
            if guess == num:
                print('WOW {}!! You have guessed it.'.format(p_nm))
                print('You took ' + str(attempt) + ' attempts to guess it right.')
                break
            
            if attempt > max_attempt:
                print('Number of attempts exceeded')
                break
            
    Attempt()


n = int(input('Enter max range: '))
num = random.randint(1,n)
max_attempt = n//6+3
max_hint = max_attempt//2-1
guess = 0
hints = 0
START(n)
