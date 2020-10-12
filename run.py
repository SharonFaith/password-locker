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

def show_credentials(user_name):
    return Credentials.display_details(user_name)

def delete_credential(user_name, app_name):
    return Credentials.delete_creden(user_name, app_name)

def main():
    print('Hi, welcome to Password Locker App')

    while True:
        print('Use the following short codes: ca - to create a new account, li - to log in to an already existing account, ex - to exit app')  
        sc = input() 
        if sc == 'ca':
            print('First name ')
            f_name = input()
            print('Last name')
            l_name = input()
            print('Email')
            email = input()
            print('Create a username')
            user_name = input()
            while check_username(user_name):
                print('That username is already taken, try another one')
                print('Create a username')
                user_name = input()
                
            print('Create a login password')
            pword = input()
            save_users(create_user(f_name, l_name, email, user_name, pword))
            print('\n')
            print('Users include: ')
            for user in User.user_list:
                print(user.username)
            print('\n')
        elif sc == 'ex':
            break
        elif sc == 'li':
            print('Username:')
            user_name = input()
            print('Password:')
            pword = input()
            print('\n')
            if check_login(user_name, pword) and User.user_list != []:
                print('You have successfully logged in')
                print('\n')
                while check_login(user_name, pword):                    
                    print('''Use the following short codes: 
                         st - to store an existing account\'s credentials,
                         cn - to create new account credentials in the app,
                         dc - to display your credentials stored in the app,
                         d - to delete account credentials you no longer need stored
                         lo - to log out  ''')
                    print('\n')
                    print('Enter short code:')
                    short_code = input()

                    if short_code == 'st':
                        print('To store existing account details: ')
                        print('\n')
                        print('Name of the application(eg twitter etc):')
                        app_name = input()
                        print('Your username in that application: ')
                        app_uname = input()
                        print('Your password for that account')
                        app_pword = input()

                        add_credential(create_credential(user_name, app_name, app_uname, app_pword))
                        print('\n')
#                        for credential in Credentials.credentials_list:
#                            print(f'Account info for {credential.app_name} added')
                    elif short_code == 'cn':
                        print('To create new account credentials:')
                        print('\n')
                        print('Name of the application you want to sign up for:')
                        app_name = input()
                        print('Username that you will use in that application:')
                        app_uname = input()
                        print('''Choose one short code:
                        sys -You want the system to generate a password for you for this new account
                        no - You want to create a password for yourself.''')
                        s_c = input()
                        if s_c == 'sys':
                            print('How long do you want the auto generated password to be. Write in numbers')
                            
                            try:
                                length = int(input())
                                app_pword = gen_pword(length)
                                add_credential(create_credential(user_name, app_name, app_uname, app_pword))
                            except ValueError:
                                print('That input was invalid. Length should be in numbers(whole numbers)')
                        elif s_c == 'no':
                            print('Enter password you would like to use: ')
                            app_pword = input()
                            add_credential(create_credential(user_name, app_name, app_uname, app_pword))
                        else:
                            print('Kindly choose the correct code, either ~sys~ or ~no~ ')

                        
                        print('\n')
#                       for credential in Credentials.credentials_list:
#                          print(f'New account info for {credential.app_name} added')
                    elif short_code == 'dc':
                        print(f'Displaying {user_name}\'s credentials:')
                        for user_credential in show_credentials(user_name):
                            print(f'Application name : {user_credential.app_name}')
                            print(f'Username in application: {user_credential.app_uname}')
                            print(f'Password of account: {user_credential.app_pword}')
                            print('\n')

                    elif short_code == 'd':
                        print('Enter the application name of the credential that you want to delete.Eg if its for twitter type twitter ')
                        app_name = input()
                        delete_credential(user_name, app_name)

                        for user_credential in delete_credential(user_name, app_name):
                            print(f'Application name : {user_credential.app_name}')
                            print(f'Username in application: {user_credential.app_uname}')
                            print(f'Password of account: {user_credential.app_pword}')
                            print('\n')
                    
                    elif short_code == 'lo':
                        break
                    else:
                        ('Kindly input correct short code for logged in functions. st, cn, dc, d or lo')



            else:
                print('\n')
                print('''Either: Check your username and password and try again! OR Create an account if you do not have an existing one then proceed to login''')
                print('\n')
             
        else:
            print('Check your input of the short codes')

    


if __name__=='__main__':
    main()
