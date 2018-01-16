'''
Make a two-player Rock-Paper-Scissors game.
(Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)

Remember the rules:
    Rock beats scissors
    Scissors beats paper
    Paper beats rock

'''
def game():
    print('Welcome to rock paper scissors game\n') #Greetings and user input
    p1 = input('Player one enter your play: ')
    p2 = input('Player two enter your play: ')

    if p1 == p2:
        print('you tied with the same guess') #check for tie
    elif p1 == 'rock':  #Branching check for winner
        if p2 == 'paper':
            print('P2 Wins, Congratulations!')
        elif p2 == 'scissors':
            print('P1 Wins, Congratulations!')
    elif p1 == 'scissors':
        if p2 == 'rock':
            print('P2 Wins, Congratulations!')
        elif p2 == 'paper':
            print('P1 Wins, Congratulations!')
    elif p1 == 'paper':
        if p2 == 'scissors':
            print('P2 Wins, Congratulations!')
        elif p2 == 'rock':
            print('P1 Wins, Congratulations!')
    new_game = input('play again? (yes or no)') #had some variable scope issues with this one
    if new_game == 'yes': #Input from user to continue or not
        game()
    elif new_game == 'no':
        quit()

game() #start the program

