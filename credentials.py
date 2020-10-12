from user import User
import random
import string
#import pyperclip

class Credentials:
    credentials_list  = []
    users_credentials = []
    def __init__(self, user_name, application_name, app_username, app_password):
        '''
        method that initiates each credential
        '''
        self.username = user_name
        self.app_name = application_name
        self.app_uname = app_username
        self.app_pword = app_password
    
    def save_creden(self):
        '''
        method that saves credentials
        '''
        Credentials.credentials_list.append(self)
    
    @classmethod
    def display_details(cls, user_name):
        '''
        method that displays a user\'s credentials
        Args:
            user_name: takes in the currently logged user
        Returns: 
            An array containing the credentials
        '''
        users_credentials = []
        for credential in cls.credentials_list:
            if credential.username == user_name:
                users_credentials.append(credential)
        return users_credentials
