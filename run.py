#!/usr/bin/env python3.6
from user import User
from credentials import Credentials

def create_user(fname, lname, email, user_name, pword):

    new_user = User(fname, lname, email, user_name, pword)
    return new_user