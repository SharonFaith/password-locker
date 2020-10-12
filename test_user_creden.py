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



if __name__=='__main__':
    unittest.main()