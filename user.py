class User:
    """
    Class that generate new instance of us user.
    """
    user_list= [] 
  
    def ___init___(self,login_username,user_password) :
    
   
        self.login_username = login_username
        self.user_password = user_password


class Credential:
    """
    class that generate new instances of credentials
    """
    credentials_list = []
    
def __init__(self,username,account_name,account_password):
    self.username= username
    self.account_name = account_name
    self.account_password= account_password
    
def save_user(self):
    """
    save_user method saves user objects into user_list
    """
    User.user_list.append(self)

def delete_credential(self):
    """
    delete_credential method to delete a saved credential from credential_list
    """
    Credential.credential_list.remove(self)