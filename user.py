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

    @classmethod
    def user_exist(cls, user_name):
        '''
        method check if a user exists

        Args:
            user_name : username entered
        Returns:
            Boolean: True if username exists in user list
        '''
        for user in cls.user_list:
            if user.username == user_name:
                return True

    @classmethod
    def login(cls, user_name, pass_word):
        '''
        method that checks that password and username match before login

        Args:
            user_name: username entered
            pass_word: password entered
        Returns:
            boolean: True or False depending on whether the login details entered match one of a user in user_list
        '''
        for user in cls.user_list:
            if user.username == user_name and user.password == pass_word :
                return True