class Choice():
    def __init__( self, choice_id, choice_message ):
        self.choice_message =choice_message
        self.choice_id = choice_id

    def __repr__( self ):
        return self.choice_message

    def get_message( self ):
        return self.choice_message

    def get_choice_id( self ):
        return self.choice_id
    
choices = [
    Choice( 1, "Leave" ),
    Choice( 2, "Flirt" ),
    Choice( 3, "Negotiate" ),
    Choice( 4, "Argue" )
]
