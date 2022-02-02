# TODO: Implement the Seeker class as follows...
import random
# 1) Add the class declaration. Use the following class comment.

class Seeker:
    """The person looking for the Hider. 
    
    The responsibility of a Seeker is to keep track of its location and distance travelled.
    
    Attributes:
        location (int): The location of the Seeker (1-1000).
    """

    def __int__(self):
        # 2) Create the class constructor. Use the following method comment.
        """Constructs a new Seeker.

        Args:
            self (Seeker): An instance of Seeker.
        """
        self.current_location = random.radiant(1,1000)
       
    def get_location(self):
        # 3) Create the get_location(self) method. Use the following method comment.
        """Gets the current location.
        
        Returns:
            number: The current location,
        """
    
        return self.current_location

    def move_location(self, location):
        # 4) Create the move_location(self, location) method. Use the following method comment.
        """Moves to the given location.

        Args:
            self (Seeker): An instance of Seeker.
            location (int): The given location.
        """
        self.current_location = location