import unittest
#import pyperclip
from user import User
#from credentials import Credentials

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


if __name__=='__main__':
    unittest.main()