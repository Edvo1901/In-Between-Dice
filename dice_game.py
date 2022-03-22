import random

def display_details():
    print('Author : Vi Dong (Edward) Vo'
          '\nEmail ID : DongVo1901@gmail.com')

def display_dice(die1,die2,die3):
    print('+-------------------------------------+'
          '\n|',format('Die1','^9s'), '|',format('','^11s'), '|',format('Die2','^9s'), '|'
          '\n|',format(die1,'^9d'),'|', format(die3,'^11d'),'|',format(die2,'^9d'),'|'
          '\n+-------------------------------------+')

def get_play_again(display_str):
    # Update loop control
    play_again = input(display_str)

    while play_again.upper() != 'Y' and play_again.upper() != 'N':
        play_again = input('Please enter either \'y\' or \'n\': ')

    # This return is to get the valid of play_again so i can print it out later (not to break the while loop)
    return play_again

def display_Score():
    print('\nGame Summary')
    print('============')
    print('\nYou play', gameplay, 'games:')
    print('|--> Game won:', win)
    print('|--> Game lost:', lose)
    print('|--> Even-steven:', even)
    print('\nThanks for playing!')



# Set the chips for the player
chipBalance = 100

# Set the game that player has played
gameplay = 0

# Set the win, lose and even record
win = 0
lose = 0
even = 0

#Call function to display details
display_details()

play = get_play_again('\nWould you like to play in-between [y|n]? ')

if play.upper() == 'N':
    print('No worries... another time perhaps... :)')

while play.upper() == 'Y':

    # First random 1-12 dice roll
    die1 = random.randint(1, 12)

    # Second random 1-12 dice roll
    die2 = random.randint(1, 12)

    # Swaps the values of two dice if the face of die1 is larger than the face of die2
    if die1 > die2:
        temp = die1
        die1 = die2
        die2 = temp

    # Call the function to display the face of the first and second die
    print('\nDice rolled:')
    display_dice(die1, die2, 0)

    # Third random 1-12 dice roll
    die3 = random.randint(1, 12)


    # Checks if the die1 and die2 are the same
    if die1 == die2:
        print('\nEven-steven! Let\'s play again')
        print('Thanks for playing!')
        even += 1
        gameplay += 1

    # Checks if the die1 and die2 are different
    if die1 != die2:
        print('\nNot the same, let\'s play!')

        # Displays the number available chips
        print('\nNumber of chips:', chipBalance)

        # Ask player to enter their bet
        bet = int(input('Place your bet: '))

        # Set the range that player can bet from 0 to available chip
        while 0 >= bet or bet > chipBalance:
            print('Sorry, you may only bet what you have 0 -', chipBalance)
            bet = int(input('Place your bet: '))

        # Call the function to display the face of the first and second die
        print('\nDice rolled:')
        display_dice(die1, die2, die3)

        # Compare the value of 3 dice and display the results
        if die3 > die1 and die3 < die2:
            print('\n*** You win! ***')
            chipBalance = chipBalance + bet
            win += 1
            gameplay += 1

        elif die3 < die1 or die3 > die2:
            print('\n*** Sorry - You lose! ***')
            chipBalance = chipBalance - bet
            gameplay += 1
            lose += 1

        elif die3 == die1 or die3 == die2:
            print('\n*** You hit the post - You lose! ***')
            chipBalance = chipBalance - bet
            gameplay += 1
            lose += 1


    # Displays the amount of available chips the player has
    if chipBalance <= 0:
        print('\nYou\'re all out of chips!\n\n*** GAME OVER ***')
        play = 'n'

    else:
        print('\nYou now have', chipBalance, 'chips!')

        # Call function to update loop control
        play = get_play_again('Play again [y|n]? ')

    # Call function to display the record of games that player played
    if play.upper()=='N':
        display_Score()


