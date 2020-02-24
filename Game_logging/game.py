from response import responses, Response
from random import randrange, shuffle
from log import make_game_start_log, make_response_log, make_game_end_log

class Game():
    def __init__( self, game_id ):
        self.game_id = game_id
        self.game_responses = self.random_responses
        self.game_state = 0
        self.current_response = self.set_first_current_response
        self.choices_made = []
        self.choice_1_made = 0
        self.choice_2_made = 0
        self.choice_3_made = 0
        self.choice_4_made = 0

        make_game_start_log( 
            self.game_id, 
            self.responses_list,
            self.game_state, 
            self.current_response.response_id )

    @property
    def random_responses ( self ):
        new_responses = responses
        shuffle( new_responses )
        return new_responses

    @property
    def set_first_current_response( self ):
        return self.game_responses[0]

    @property
    def is_last_response( self ):
        return len( self.game_responses ) == self.game_responses.index( self.current_response ) + 1

    @property
    def responses_list( self ):
        response_ids = []
        for response in self.game_responses:
            response_ids.append( response.get_response_id() )
        return response_ids

    def next_response( self ):
        index = self.game_responses.index( self.current_response )
        if( not self.is_last_response ):
            self.current_response = self.game_responses[index + 1]

    def choice_made( self, choice_id ):
        if( choice_id == 1 ):
            self.choice_1_made += 1
        elif( choice_id == 2 ):
            self.choice_2_made += 1
        elif( choice_id == 3 ):
            self.choice_3_made += 1
        else:
            self.choice_4_made += 1
        self.choices_made.append( choice_id )
        
    def check_game_state( self, selected_choice_id ):
        self.choice_made( selected_choice_id )
        if ( self.current_response.wrong_choice( selected_choice_id ) ):
            self.game_state = 1

            make_game_end_log( 
                self.game_id, 
                self.responses_list, 
                self.game_state, 
                self.choices_made )

            make_response_log( 
                self.game_id, 
                self.choice_1_made, 
                self.choice_2_made,
                self.choice_3_made, 
                self.choice_4_made )
        elif( self.is_last_response ):
            self.game_state = 2

            make_game_end_log( 
                self.game_id, 
                self.responses_list, 
                self.game_state, 
                self.choices_made )

            make_response_log( 
                self.game_id, 
                self.choice_1_made, 
                self.choice_2_made,
                self.choice_3_made, 
                self.choice_4_made )
        else:
            self.next_response()
        



