import unittest
#import pyperclip
from user import User
from credentials import Credentials

class TestUser(unittest.TestCase):
    """
    Test class that defines test cases for the user class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases.
    
    """
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User('Patrick', 'Rodgers', 'patrodg@email.com', 'pat_rodge', 'pal1234')
        #creates user object
    
    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        User.user_list = []

    def test_init(self):
        '''
        to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.first_name, 'Patrick')
        self.assertEqual(self.new_user.last_name, 'Rodgers')
        self.assertEqual(self.new_user.email, 'patrodg@email.com')
        self.assertEqual(self.new_user.username, 'pat_rodge')
        self.assertEqual(self.new_user.password, 'pal1234')
    
    def test_save_user(self):
        '''
        to test if a new user can be saved to the list of users
        '''
        self.new_user.save_user()

        self.assertEqual(len(User.user_list), 1)


    def test_save_multiple_users(self):
        '''
        to test if more than one user can be added to the list of users
        '''
        self.new_user.save_user()
        test_user = User('Yod', 'Ger', 'yod@email.com', 'anon', 'pal1234')
        test_user.save_user()

        self.assertEqual(len(User.user_list), 2)

    def test_user_exists(self):
        '''
        to test if a user already exists
        '''
        self.new_user.save_user()
        test_user = User('Yod', 'Ger', 'yod@email.com', 'anon', 'pal1234')
        test_user.save_user()

        user_exists = User.user_exist('anon')
        self.assertTrue(user_exists)

    def test_login(self):
        '''
        to test if current user is indicated on login
        '''

        self.new_user.save_user()
        test_user = User('Yod', 'Ger', 'yod@email.com', 'anon', 'pal1234')
        test_user.save_user()

        user_logged = User.login('anon', 'pal1234')
        self.assertTrue(user_logged)

class TestCredentials(unittest.TestCase):
    '''
    Test class that defines test cases for user credential behaviours
    '''
    def setUp(self):
        '''
        setup method to run before each test case
        '''
        self.new_creden = Credentials('pat_rodge', 'twitter', 'pat12', '1234')

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        Credentials.credentials_list = []

    def test_init(self):
        '''
        test to check if credentials objects is initialized properly
        '''

        self.assertEqual(self.new_creden.username, 'pat_rodge')
        self.assertEqual(self.new_creden.app_name, 'twitter')
        self.assertEqual(self.new_creden.app_uname, 'pat12')
        self.assertEqual(self.new_creden.app_pword, '1234')

    def test_add_details(self):
        '''
        test to check if a user can save existing account credentials
        '''
        self.new_creden.save_creden()

        self.assertEqual(len(Credentials.credentials_list), 1)

    def test_add_multiple_details(self):
        '''
        test to check if multiple credentials can be added
        '''
        self.new_creden.save_creden()
        another_creden = Credentials('pat_rodge', 'facebook', 'pat11', '12345')
        another_creden.save_creden()

        self.assertEqual(len(Credentials.credentials_list), 2)

if __name__=='__main__':
    unittest.main()