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
def existing_credentials(name):
    '''
    Functiion that checks if an account really exists
    '''
    return Credential.credential_exist(name)


def delete_credential(credentials):
    '''
    Function that deletes credentials that are no longer in use
    '''
    return Credential.delete_credential(credentials)


def display_credential():
    '''
    Functiomn that displays all the saved credentials 
    '''
    return Credential.display_credentials()
def main():
    while True:
        print("*** PASSWORD LOCKER ***")
        print('_'*30)
        print("Do you have an account with password Locker? y/n")
        print("use short 'ex' to  log out")
        option = input().lower()
        if option == "y":

            print('*** Login ***')
            print('Enter username \n')
            nomname = input()
            print('\n')
            print('Enter password')
            nompass = input()
 print(f"Welcome:{nomname} to your Account ")
            print('*'*40)

            print("Select an option either 1,2,3,4 or 5")
            print('\n')

            while True:
                    print('1:Add credential')
                    print('2:View saved credential')
                    print('3:Delete Credentials')
                    print('4:Search Credentials')
                    print('5:Leave')
                    selected = input()if selected == '1':
                        while True:
                            print('Do you want to proceed? y/n')

                            decision = input().lower()
                            if decision == 'y':
                                print("Enter Account name")
                                accname = input()
                                print("Enter username")
                                uname = input()
                                print("Enter a password")
                                print(
                                    "Do you want a computer generated password ? use 'gp' or 'new' to create your own ")
                                word = input().lower()
                                if word == 'gp':
                                    accpass = random.randint(0, 1000)
                                    print(
                                        f"Account:{accname} Username: {uname} Password:{accpass}")
                                    print('\n')
                                elif word == 'new':
                                    print("Create password")
                                    accpass = input()
                                    print(
                                        f"Account:{accname} Password:{accpass}")
                                    elif decision == 'n':
                                break
                            else:
                                print(
                                    "Wrong choice use  either y to continue or n to stop")
                    elif selected == '2':
                        while True:
                            print('view your credenttial below')
                            if display_credential():

                                for credential in display_credential():
                                    print(
                                        f"Account Name:{creds.account_name} Username: {creds.username} Password:{creds.account_password}")

                            else:
                                print('\n')
                                print(
                                    "You don't have any saved credential before \n")

                            print("Do you want to go back yes/no")

                            reverse = input().lower()

                    
if __name__ == '__main__':
    main()