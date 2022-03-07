from password_data import PasswordData
from datetime import datetime
from typing import TypeVar

TTimePasswordData = TypeVar("TTimePasswordData", bound="TimePasswordData")


class TimePasswordData(PasswordData):
    def __init__(self, username, password):
        """
        Inizialise (inherit) the parent Password data class and create a
        new specific attribute (timestamp) for the TimePasswordData class.
        This attribute should be made private to remove write access for users
        of this class.

        Attributes:
            public:
                username            --  Inherited from PasswordData 
                password            --  Inherited from PasswordData
                encrypted_password  --  Inherited from PasswordData
            
            private:
                timestamp           --  The current date and time. 
                                        Use datetime.now() to get a date object.
                                        See dir(datetime.now()) for object attributes.
                                        As an example: To access the current month
                                        use datetime.now().month
               
        """
        pass # Implement your init method here, remove pass
    
    def update_username(self, new_username: str):
        """
        Update the username attribute with a new_username.
        The username can only be updated if the object instance was 
        NOT created on christmas eve (12/24). Use the timestamp 
        attribute to check this condition.
        
        """
        pass # Implement your method here, remove pass

    def __eq__(self, other: TTimePasswordData) -> bool:
        """
        Implement a == operator for the TimePasswordData class.
        Try to use the __eq__ operator from the PasswordData class
        when implementing this magic method.  
        """ 
        pass # Implement your magic method here, remove pass


    if __name__ == "__main__":
        tpd1 = TimePasswordData("Super_username", "strong_password")
        tpd2 = TimePasswordData("Another_super_username", "second_strong_password")

        tpd1.update_username("a_better_username")

        print(tpd1 == tpd2)
        