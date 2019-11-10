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

if __name__ == '__main__':
    unittest.main()