import random
import math 
import sys




#Pick random nummbers for all levels
pick_easy = random.randint(1, 10)
pick_medium = random.randint(1, 50)
pick_hard = random.randint(1, 100)

    


#For user responses
yes_list = ['y', 'yes', 'yep', 'yup','yeah', 'totally','totes', 'sure', 'you bet', 'ok', 'k', 'okie dokie', 'alright', 'sounds good', 'ye']
no_list = ['n', 'no', 'naw', 'nope', 'nah', 'not this time']

 

#greeting user
def greeting():
    print('Hello There!')



def intro():
    res = input('Do you want to play a game?\n[y]\n[n]\n')
    if res.lower() in yes_list:
        print('Alright, let\'s play')
        start()
    elif res.lower() in no_list:
        print('Alright, we\'ll play next time')
    else:
        print('I\'m sorry, I didn\'t understand, please provide a valid answer.')
        return intro()


#to start
def start():
    res = input('We will start on easy, and then work our way to hard. Are you ready?\n')
    if res.lower() in yes_list:
        print('Okay, let\'s get it')
        guess_one_easy()
    elif res.lower() in no_list:
        print('Ok, next time then!')
    else:
        print('Please provide a valid response.')
        start()


#to move on to the next level
def level_two():
    res = input('Okay, good job! It will only get harder from here. Are you ready?\n')
    if res.lower() in yes_list:
        print('Let\'s get to it!')
        guess_one_medium()
    elif res.lower() in no_list:
        print('Ok, bye!')
        sys.exit()
    else:
        print('Type in a valid response')
        level_two()


def level_three():
    res = (input('Great job, but the hardest is yet to come! Are you ready?\n'))
    if res.lower() in yes_list:
        print('Ok, let\'s get started!')
        guess_one_hard()
    elif res.lower() in no_list:
        print('Ok, I understand. See you!')
        sys.exit()
    else:
        print('Please provide a valid response.')
        level_three()



#create level one
def guess_one_easy():
    while True:
        try: 
            tries = 0
            print(pick_easy)
            res = int(input('Pick a number between 1 and 10!\n'))
            if res > 10 or res < 1:
                print('That number is not in the range')
                guess_one_easy()
            elif abs(res - pick_easy) == 1:
                print('You are very close (within one)! Guess again. You have two lives left!')
                tries += 1
                guess_two_easy()
            elif 2 <= abs(res - pick_easy) <= 5:
                print('A little off (within 5)! Two lives left.')
                tries += 1
                guess_two_easy()
            elif abs(res- pick_easy) > 5:
                print('Way off! Try again. You have two lives left')
                guess_two_easy()
            else:
                print('You got it!!')
                tries += 1
                print(f'number of attempts taken: {tries}')
                move_on_easy()
        except ValueError:
            print('That is not a number.')
            guess_one_easy()
            



#guess two for easy
def guess_two_easy():
    while True:
        try:
            tries = 1
            print(pick_easy)
            res = int(input())
            if res > 10 or res < 1:
                print('That number is not in the range, pick again')
                guess_two_easy()
            elif res != pick_easy and pick_easy % 2 == 0:
                print('Hint: The number I am thinking of is even. One life left!')
                tries += 1
                guess_three_easy()
            elif res != pick_easy and pick_easy % 2 == 1:
                print('Hint: The number I am thinking of it odd. One life left!')
                tries += 1
                guess_three_easy()
            else:
                print('You got it!!')
                tries += 1
                print(f'number of attempts taken: {tries}')
                move_on_easy()
        except ValueError:
            print('That is not a number. Pick again')
            guess_two_easy()


#guess three for level one
def guess_three_easy():
    while True:
        try:
            res = int(input())
            print(pick_easy)
            tries = 2
            if res > 10 or res < 1:
                print('That number is not in the range, pick again')
                guess_three_easy()
            elif res != pick_easy:
                tries += 1
                print(f'I\'m sorry, you lost!! The number was {pick_easy}')
                print('play again next time!')
                sys.exit()
            else:
                print('You got it!!')
                tries += 1
                print(f'number of attempts taken: {tries}')
                move_on_easy()
        except ValueError:
            print('That is not a number. Pick again')
            guess_three_easy()




#create medium level
def guess_one_medium():
    while True:
        try:
            tries = 0
            print(pick_medium)
            res = int(input('This is where the fun begins! Pick a number between 1 and 50\n'))
            if res == pick_medium:
                print('Holy shit you got it on the first guess!!')
                tries += 1
                print(f'Number of attempts taken: {tries}')
                move_on_medium()
            elif abs(res - pick_medium) <= 10:
                print('You are within 10!')
                print('Four lives left!')
                tries += 1
                guess_two_medium()
            elif 10 < abs(res- pick_medium) <= 20:
                print('You are within 20!')
                print('Four lives left!')
                tries += 1
                guess_two_medium()
            elif 20 < abs(res - pick_medium) <= 30:
                print('you are within 30!')
                print('Four fives left!!')
                tries += 1
                guess_two_medium()
            elif 30 < abs(res - pick_medium) <= 40:
                print('You are within 40!')
                print('Four lives left')
                tries += 1
                guess_two_medium()
            elif 40 < abs(res - pick_medium) <= 50:
                print('Holy shit way off!! You are within 50 of the guess!!')
                print('Four lives left')
                tries += 1
                guess_two_medium()
            else:
                print('That number is out of the range, pick again!')
                guess_one_medium()
        except ValueError:
            print('That is not a number')
            guess_one_medium()



#guess two for medium level
def guess_two_medium():
    while True:
        try:
            tries = 1
            res = int(input())
            if res < 1 or res > 50:
                print('That is not in the range. Pick again!\n')
                guess_two_medium()
            elif res > pick_medium:
                print('Your pick was higher than the number that I am thinking of! Try again.')
                print('Three lives left')
                tries += 1
                guess_three_medium()
            elif res < pick_medium:
                print('Your pick was lower than the number that I am thinking of! Try again.')
                print('Three lives left')
                tries += 1
                guess_three_medium()
            else:
                print('You got it champ!!')
                tries += 1
                print(f'Number of attempts taken: {tries}')
                move_on_medium()
        except ValueError:
            print('That is not a number')
            guess_two_medium()




#define hints for guess three
hint_one = random.randint(1, 15)
hint_two = random.randint(1, 15)
hint_one_main = pick_medium - hint_one
hint_two_main = pick_medium + hint_two



#guess three for medium
def guess_three_medium():
    while True:
        try:
            tries = 2
            res = int(input())
            if res < 1 or res > 50:
                print('That is not in the range. Pick again.\n')
                print('Two lives left!')
                guess_three_medium()
            elif res != pick_medium and hint_one_main < 0:
                print(f'The number is somewhere in between {hint_one_main} and {hint_two_main}(Excluding negative values)')
                print('Two lives left!')
                tries += 1
                guess_four_medium()
            elif res != pick_medium and hint_two_main > 50:
                print(f'the number is somewhere in between {hint_one_main} and {hint_two_main}(Not including values over 50)')
                print('Two lives left!')
                tries += 1
                guess_four_medium()
            elif res != pick_medium:
                print(f'The number is somewhere in between {hint_one_main} and {hint_two_main}')
                print('Two lives left!')
                tries += 1
                guess_four_medium()
            else:
                print('You got it woohooo!')
                tries += 1
                print(f'Number of attempts taken: {tries}')
                move_on_medium()
        except ValueError:
            print('That is not a number')
            guess_three_medium()


#guess four for medium
def guess_four_medium():
    while True:
        try:
            tries = 3
            res = int(input())
            if res < 1 or res > 50:
                print('That is not in the range. Pick again!')
                guess_four_medium()
            elif res != pick_medium:
                print(f'Final hint! The number you picked is {abs(res - pick_medium)} away from the number I am thinking of!')
                print('One life left!')
                guess_five_medium()
            else:
                print('Wow. I thought you wouldn\'t get it!!')
                tries += 1
                print(f'Number of attempts taken: {tries}')
                move_on_medium()
        except ValueError:
            print('That is not a number.')
            guess_four_medium()
        


#guess five for medium. Last guess
def guess_five_medium():                         
    while True:
        try:
            tries = 4
            res = int(input())
            if res != pick_medium:
                tries += 1
                print(f'I\'m sorry, you lost!! The number was {pick_medium}')
                print('Try again next time!!')
                sys.exit()
            else:
                print('Wow. I thought you wouldn\'t get it!!')
                tries += 1
                print(f'Number of attempts taken: {tries}')
                move_on_medium()
        except ValueError:
            print('That is not a number.')
            guess_five_medium()



#Hard level
def guess_one_hard():
    while True:
        try:
            tries = 0
            print(pick_hard)
            res = int(input('Pick a number between 1 and 100\n'))
            if res == pick_hard:
                print('Holy shit! How the fuck did you do that!! First Try!')
                tries += 1
                print(f'Number of attempts taken: {tries}')
                winner()
            elif abs(res - pick_hard) <= 20:
                print('You are within 20!(0-20) You are very close!')
                print('Five lives left!')
                tries += 1
                guess_two_hard()
            elif 20 < abs(res - pick_hard) <= 40:
                print('You are within 40!(20-40) You are close!')
                print('Five lives left!')
                tries += 1
                guess_two_hard()
            elif 40 < abs(res - pick_hard) <= 60:
                print('You are within 60!(40-60)')
                print('Five lives left!')
                tries +=1
                guess_two_hard()
            elif 60 < abs(res - pick_hard) <= 80:
                print('You are within 80!(60-80)')
                print('Five lives left!')
                tries += 1
                guess_two_hard()
            elif 80 < abs(res - pick_hard) <= 100:
                print('You are withing 100!(80-100) Way off!!')
                print('Five lives left!')
                tries += 1
                guess_two_hard()
            else:
                print('That is not in the range! Pick again.')
                guess_one_hard()
        except ValueError:
            print('That is not a number')
            guess_one_hard()
        

#guess two for hard
def guess_two_hard():
    while True:
        try:
            tries = 1
            res = int(input())
            if res < 1 or res > 100:
                print('That number is not in the range. Pick again.')
            elif pick_hard % 2 == 0 and res != pick_hard:
                print('The number that I am thinking of is even. Try again.')
                print('Four lives left!')
                tries += 1
                guess_three_hard()
            elif pick_hard % 2 == 1 and res != pick_hard:
                print('The number that I am thinking of is odd. Try again.')
                print('Four lives left!')
                tries += 1
                guess_three_hard()
            else:
                print('You\'ve guessed it!!! Great job')
                tries += 1
                print(f'Number of attempts taken: {tries}')
                winner()
        except ValueError:
            print('That is not a number.')
            guess_two_hard()


#guess three for hard
def guess_three_hard():
    while True:
        try:
            tries = 2
            res = int(input())
            if res < 1 or res > 100:
                print('That number is not in the range. Pick again.')
                guess_three_hard()
            elif res > pick_hard:
                print('The number you picked is bigger than the number I am thinking of!')
                print('Three lives left!')
                tries +=1
                guess_four_hard()
            elif res < pick_hard:
                print('The number you picked is smaller than the number I am thinking of!')
                print('Three lives left!')
                tries += 1
                guess_four_hard()
            else:
                print('You\'ve got it!!')
                print(f'Number of attempts taken: {tries}')
                winner()
        except ValueError:
            print('That is not a number')
            guess_three_hard()

#make hints for guess four
hard_num_two = random.randint(1, 20)
hard_num_two = random.randint(1, 20)
hard_hint = pick_hard - hint_one
hard_hint_two = pick_hard + hard_num_two


#guess four for hard
def guess_four_hard():
    while True:
        try:
            tries = 3
            res = int(input())
            print(hard_hint_two)
            greater_than_hundred = int(str(int(hard_hint_two))) - int(str(int(hard_hint_two))[-1])
            greater_than_ten = (int(str(int(hard_hint_two))) - int(str(int(hard_hint_two))[-2:]))
            square_root = math.sqrt(pick_hard).is_integer()
            if square_root and res != pick_hard:
                print('The number I am thinking of is a perfect square')
                print('Two lives left!')
                tries += 1
                guess_five_hard()
            elif square_root == False and hard_hint < 1 and res != pick_hard:
                print(
                    f'The number I am thinking of is in between {hard_hint + abs(hard_hint)} and {hard_hint_two}')
                print('Two lives left')
                tries += 1
                guess_five_hard()
            elif square_root == False and 110 > hard_hint_two and hard_hint_two > 100 and res != pick_hard:
                print(f'The number I am thinking of is in between {hard_hint} and {greater_than_hundred}')
                print('Two lives left!')
                tries += 1
                guess_five_hard()
            elif square_root == False and hard_hint_two >= 110 and res != pick_hard:
                print(f'The number I am thinking of is in between {hard_hint} and {greater_than_ten}')
                print('Two lives left!')
                tries += 1
                guess_five_hard()
            elif square_root == False and hard_hint_two < 100 and hard_hint > 1 and res != pick_hard:
                print(f'The number I am thinking of is in between {hard_hint} and {hard_hint_two}')
                print('Two lives left!')
                tries += 1
                guess_five_hard()
            elif res == pick_hard:
                print('You\'ve got it man!')
                tries += 1
                print(f'Number of attempts taken: {tries}')
                winner()
            else:
                print('That number is not in the range! Pick again!')
                guess_four_hard()
        except ValueError:
            print('That is not a number.')
            guess_four_hard()



#guess five hard
def guess_five_hard():
    while True:
        try:
            tries = 4
            dividing_number = random.randint(1, 10)
            print(dividing_number)
            res = int(input())
            if res <1 or res > 100:
                print('That number is not in the range. Pick again.')
                guess_five_hard()
            elif res != pick_hard:
                print(f'when I divide my number and a random number, I approximately get {round(pick_hard / dividing_number)}')
                guess_six_hard()
            else:
                print('You finally got it!!!!')
                tries += 1
                print(f'Number of attempts taken: {tries}')
                winner()
        except ValueError:
            print('That is not a number.')
            guess_five_hard()
    



#guess six for hard. Last hint
def guess_six_hard():
    while True:
        try:
            tries = 5
            res = int(input())
            if res < 1 or res > 100:
                print('That number is not in the range. Pick again.')
            elif res != pick_hard:
                print(f'I\'m sorry. The number was {pick_hard}')
                print('So close! Try again soon!')
                sys.exit()
            else:
                print('Wooohoo! You finally got it!')
                tries += 1
                print(f'number of attempts taken: {tries}')
                winner()
        except ValueError:
            print('That is not a number.')
            guess_six_hard()

    

#set up moving on for all levels
def move_on_easy():
    res = input('Are you ready to proceed?\n')
    if res.lower() in yes_list:
        level_two()
    elif res.lower() in no_list:
        print('Ok. Have a nice day!')
        sys.exit()
    else:
        print('Please provide a valid statement.')
        move_on_easy()



def move_on_medium():
    res = input('Are you ready to proceed?\n')
    if res.lower() in yes_list:
        level_three()
    elif res.lower() in no_list:
        print('Ok. Have a nice day!')
        sys.exit()
    else:
        print('Please provide a valid statement.')
        move_on_medium()



def winner():
    print('You beat me! Impresive!')
    print('Play again soon!')
    sys.exit() 
    
 




greeting()
intro()



