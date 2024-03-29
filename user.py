class User:
    """
    Class that generate new instance of us user.
    """
    user_list = []

    def ___init___(self, login_username, user_password):
        '''
        initiating the variables
        '''
        self.login_username = login_username
        self.user_password = user_password

    def save_user(self):
        """
        save_user method saves user objects into user_list
        """
        User.user_list.append(self)
    
    @classmethod
    def user_exists(cls, login_username):
        '''
        Method that checks if a credential object exists from the credential  list.
        Args:
            acc_name: Account  to search if it exists
        Returns :
            Boolean: True or false depending if the object exists
        '''

        for user in cls.user_list:
            if user.login_username == login_username:
                return True
        return False

    
class Credential:
    """
    class that generate new instances of credentials
    """
    credentials_list = []

    def __init__(self, username, account_name, account_password):
        self.username = username
        self.account_name = account_name
        self.account_password = account_password

    def save_credential(self):
        """
        save_credential method  saves credential into credential_list
        """
        Credential.credentials_list.append(self)

    def delete_credentials(self):
        """
        delete_credential method to delete a saved credential from credential_list
        """
        Credential.credentials_list.remove(self)

    @classmethod
    def find_by_name(cls, account_name):
        """
        method that takes in a account name and returns a returns a credential that matches that account name

        Args:
            account_name:account name to search for 
        Returns:
                credential of user that matche  the account name
        """
        for credential in cls.credentials_list:
            if credential.account_name == account_name:
                return credential

    @classmethod
    def credential_exists(cls, acc_name):
        '''
        Method that checks if a credential object exists from the credential  list.
        Args:
            acc_name: Account  to search if it exists
        Returns :
            Boolean: True or false depending if the object exists
        '''

        for credential in cls.credentials_list:
            if credential.account_name == acc_name:
                return True
        return False

    @classmethod
    def display_credentials(cls):
        '''
        Method which will display the credential list
        '''
        return cls.credentials_list
