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