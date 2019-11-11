import unittest  # Importing the unittest module
from user import User  # Importing class user
from user import Credential


class TestUser(unittest.TestCase):

    """
    Test class that defines test cases for the user class behaviours.

    Args:
         unittest.TestCase:TestCase that help in creating test cases
    """

    def setUp(self):
        """
        set up method to run before each test cases.
        """
        # self.new_user = User("owinolawrence", "2019")
        self.new_credential = Credential("owinolawrence", "twitter", "2018")

    def test_init(self):
        """
        test_init test case to test if the object is initialized properly
        """
        # self.assertEqual(self.new_user.login_username, "owinolawrence")
        # self.assertEqual(self.new_user.user_password, "2019")
        self.assertEqual(self.new_credential.account_name, "twitter")
        self.assertEqual(self.new_credential.account_password, "2018")

    def test_save_object(self):
        """
        test_save_object test case to test if the object will be save in user list and credential list
        """
        # self.new_user.save_detail()
        # self.new_credential.save_credential()

        # self.assertEqual(len(User.user_list), 1)
        # self.assertEqual(len(Credential.credential_list), 1)

    def tearDown(self):
        """
        tearDown method that does clean up after test case has run.
        """
        User.user_list = []
        Credential.credential_list = []

    def test_delete_user(self):
        """
        test_delete_user to test if we can remove a user from the user list
        """

    def test_delete_credentials(self):
        """
        test to check if the user can delete his or her credentials
        """
        self.new_credential.save_credential()
        test_credential = Credential("owinolawrence", "instragram", "2017")
        test_credential.save_credential()
        self.new_credential.delete_credentials()  # Deleting a credential object
        # self.assertEqual(len(Credential.credential_list), 1)

    def test_find_user_by_name(self):
        """
        test to check if we can find a user by using  account name and display information
        """
        self.new_credential.save_credential()
        test_credential = Credential("owinolawrence", "twitter", "2018")
        test_credential.save_credential()
        found_credential = Credential.find_by_name("twitter")
        self.assertEqual(found_credential.account_password, "2018")

    def test_credential_exists(self):
        """
        test to check if we can return a Boolean if we cannot find the account name
        """
        self.new_credential.save_credential()
        test_credential = Credential("owinolawrence", "twitter", "2018")
        test_credential.save_credential()
        credential_exist = Credential.credential_exists("twitter")
        self.assertTrue(credential_exist)

    def test_display_all_credential(self):
        '''
        method that return all the credential saved
        '''

        self.assertEqual(Credential.display_credentials(),
                         Credential.credentials_list)


if __name__ == '__main__':
    unittest.main()
