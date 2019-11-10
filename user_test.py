import unittest #Importing the unittest module
from user import User # Importing class user

class TestUserss(unittest.TestCase):
    """
    Test class that defines test cases for the user class behaviours.
    
    Args:
         unittest.TestCase:TestCase that help in creating test cases
    """
         
def setUp(self):
    """
    set up method to run before each test cases.
    """
    self.new_username = User("owinolawrence")

def test_init(self):
    """
    test_init test case to test if the object is initialized properly
    """
    self.assertEqual(self.new_username.login_username,"owinolawrence")

def test_save_object(self):
    """
    test_save_object test case to test if the object will be save in user list and credential list
    """
    self.new_user.save_detail()
    self.new_credential.save_credential()
    
    self.assertEqual(len(User.user_list),1)
    self.assertEqual(len(Credential.credential_list),1)

if __name__ == '__main__':
    unittest.main()