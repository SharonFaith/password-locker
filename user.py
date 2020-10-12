class User:
    '''
    Class that generates new instances of user
    '''
    user_list = []

    def __init__(self, first_name, last_name, email, username, password):
        '''
        method that initiates instances of User class
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.username = username
        self.password = password

    def save_user(self):
        '''
        method that saves users to user list
        '''
        User.user_list.append(self)