# A handful of functions to support seeing what Python thinks is a number
# AUTHOR: LT
# EMAIL: See end of slides



# HINT: *import* borrows existing code from somewhere else
import math



# Global variables... HINT: which means available anywhere in this file.
thisIsntANumber = 17
thisIsANumber = "psych! It's actually a string (of letters)"



def is_number(n):
    """Returns True if n is a number and false otherwise
    
    NOTE: This function is an inversion of the standard isnan (Is Not a Number)
    function. Generally, I find asking questions in the positive 
    more intuitive.
    """
    
	return not math.isnan(n)



def number_verification_service():
    """Verify that user input is a number
    
    As a service, this function asks for user input and verifies until 
    terminated
    """

    # NOTE: while ( True ) means that this loops "forever"
    while ( True ):
        user_entity = input("Enter something to verify if it is a number: ")
        
        if is_number( user_entity ):
            print( "Number Verified: " + str( user_entity ) )
            
        else:
            print( "Not a Number." )



# Starts the number verification service
number_verification_service()