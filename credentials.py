from user import User
from user import Credential
import random
def create_user(username, password):
    """
    function that create enable a person to create a new user
    """
    new_user = User(username,password)
    return new_user

def save_user(user):
    """
function that save new created user
    """
    user.save_user()

def find_credential(account_name):
    '''
    Function that finds credentials by account name
    '''

    return Credential.find_by_name(account_name)


 
if __name__ == '__main__':
    main()