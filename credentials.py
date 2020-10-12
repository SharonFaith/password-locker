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

    @classmethod
    def delete_creden(cls, user_name, app_name):
        '''
        method that deletes a user\'s particular credential

        Args:
            user_name: current user username
            app_name: inputted app name to be deleted
        Returns:
            an array that displays the users credentials minus the one deleted

        '''
        users_credentials = []
        for credential in cls.credentials_list:
            if credential.username == user_name:
                users_credentials.append(credential)
                if credential in users_credentials:
                    if credential.app_name == app_name:
 #                       users_credentials.remove(credential)
                        Credentials.credentials_list.remove(credential)
        return users_credentials

    def generate_password(length):
        '''
        method that generates a random password

        Args:
            length: the length the user wants the password to be
        Returns:
            random alphanumeric string
        '''
        letters_digits = string.ascii_lowercase + string.digits
        result = ''.join((random.choice(letters_digits) for i in range(length)))
        return result
    