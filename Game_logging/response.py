class Response():
    def __init__( self, response_id, response_message, wrong_choice_id ):
        self.response_id  =response_id
        self.response_message = response_message
        self.wrong_choice_id = wrong_choice_id

    def __repr__( self ):
        return self.response_message

    def get_response_id( self ):
        return self.response_id

    def wrong_choice( self, choice_made_id ):
        return choice_made_id == self.wrong_choice_id

responses = [
    Response( 1, "", 3 ),
    Response( 2, "", 4 ),
    Response( 3, "", 1 ),
    Response( 4, "", 2 ),
    Response( 5, "", 1 )
]

print( responses )