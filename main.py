
# import random module
import random

def play():
    # possible game moves
    game_move = ['r', 'p', 's']

    # player move input selection
    player_move =  input('Select an option to play: \n r for rock, \n p for paper, and \n s for scissors \n')
    #  convert player move to lowercase
    player_move = player_move.lower()
    # cpu random move
    cpu_move = random.choice(game_move)

    # looping untill a valid input
    while player_move not in game_move:
        player_move = input('Error! invalid selection: \n Please select a valid input \n r for rock, \n p for paper, and \n s for scissors: \n ')
        # convert player move to lowercase
        player_move = player_move.lower()

    # # assigning player move to rock paper and scissors
    if player_move == 'r':
        player_move = 'Rock'
    elif player_move == 'p':
        player_move = 'Paper'
    elif player_move == 's':
        player_move = 'Scissors'

    # # assigning computer move to rock paper and scissors
    if cpu_move == 'r':
        cpu_move = 'Rock'
    elif cpu_move == 'p':
        cpu_move = 'Paper'
    elif cpu_move == 's':
        cpu_move = 'Scissors'

    # game moves for each game
    print(f'Game moves: Player ({player_move}) : CPU ({cpu_move}).')

    # condition for tie
    if player_move == cpu_move:
        print(f"Both players draw with: {player_move}!. It's a tie!")
        # restart game
        play()
    
    # condition for winning 
    elif player_move == 'Rock':
        if cpu_move == 'Scissors':
            winner = player_move
        else:
            winner = cpu_move
    elif player_move == 'Paper':
        if cpu_move == 'Rock':
            winner = player_move
        else:
            winner = cpu_move
    elif player_move == 'Scissors':
        if cpu_move == 'Paper':
            winner = player_move
        else:
            winner = cpu_move
    
    # printing the winner
    if winner == player_move:
        print(f'Player wins game with: {player_move}')
    elif winner == cpu_move:
        print(f'CPU wins game with: {cpu_move}')

    # to play again
    def play_again ():
        redo = input ('To play again:\n type N for No: \n or Y for Yes: \n')

        if(redo.lower() == 'y'):
            play()
        elif(redo.lower() != 'y'):
            print('Thank you, for playing!')
        # else:
        #     pass

    play_again()

play()


