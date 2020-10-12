#!/usr/bin/env python3.6
from user import User
from credentials import Credentials

def create_user(fname, lname, email, user_name, pword):

    new_user = User(fname, lname, email, user_name, pword)
    return new_user

def save_users(user):
    user.save_user()
    
def check_username(user_name):
    return User.user_exist(user_name)

def check_login(user_name, pass_word):
    return User.login(user_name, pass_word)

def create_credential(user_name, app_name, app_uname, app_pword):
    new_credential = Credentials(user_name, app_name, app_uname, app_pword)
    return new_credential

def add_credential(credentials):
    Credentials.save_creden(credentials)

def gen_pword(length):
    gen_pwords = Credentials.generate_password(length)
    return gen_pwords
