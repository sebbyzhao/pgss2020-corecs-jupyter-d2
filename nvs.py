# What Would Python Determine?
# does Python think the user input is a number?

# _Imports_ borrow code from elsewhere
import math

# Global variables
thisIsntANumber = 17

def is_number(n):
	return not math.isnan(n)



### BOOKMARK : loop, ask user for input, check is_number
def number_verification_service():
    while ( True ):
        user_entity = input("Enter something to verify if it is a number: ")
        
        if is_number( user_entity ):
            print( "Number Verified: " + str( user_entity ) )
            
        else:
            print( "Not a Number." )



number_verification_service()