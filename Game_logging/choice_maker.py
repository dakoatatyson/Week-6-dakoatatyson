from game import Game
from response import Response
from choice import Choice, choices

def new_game():
    games = []

    game = Game(0)

    while ( game.game_state == 0 ):
        print( game.current_response )
        print( "Chose one:  " )
        for choice in choices:
            print(choice)

        choice = int( input( "Chose 1, 2, 3, or 4\n" ) )

        game.check_game_state( choice )

    print(game.choices_made)


