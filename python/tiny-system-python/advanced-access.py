#!/usr/bin/env python2
# _*_ coding: utf-8 _*_

import os
import time


info_interface_main = """
Welcome to tiny-system-python
'r' to register
'i' to login
'q' to quit
"""

info_interface_register = """

"""

info_interface_login = """

""" 

accounts_file_path = '/tmp/account/'

def check_accounts_file(account_name):
    if os.path.isdir(accounts_file_path):
        pass
    else:
        os.mkdir(accounts_file_path)
    if os.path.exists(accounts_file_path+account_name+'.txt'):
        return True
    else:
        return False

# body of main
while True:
    # body of sub-mian
    
    # chance: allow user try %chance time when enter account's password.
    chance = 3
    
    # choice: decide whice sub-main you want enter.
    choice = raw_input(info_interface_main+'>>>')

    # body of register
    if 'r' == choice:
        input_user_name = raw_input('UserName:')
        if input_user_name == '':
            print 'fail to register a system account'
        # elif os.path.exists(accounts_file_path+input_user_name+'.txt'):
        elif check_accounts_file(input_user_name):
            print '\033[35;1muser name %s has been registered!, please change another>>>\033[0m' % input_user_name
        else:
            account_file = open(accounts_file_path+input_user_name+'.txt','w')
            while True:
                input_password = raw_input('Password:')
                if input_password != '':
                    account_file.write(input_password)
                    account_file.flush()
                    account_file.close()
                    print 'Your account named %s has been registered successfully!' % input_user_name
                    input_user_name = ''
                    input_password = ''
                    break
                else:
                    print 'password invalid, try again'
    # /body of register

    # body of login
    elif 'i' == choice:
        input_user_name = raw_input('UserName:')
        if input_user_name == '':
            print 'invalid account name'
        # elif os.path.exists(accounts_file_path+input_user_name+'.txt'):
        elif check_accounts_file(input_user_name):
            account_file = open(accounts_file_path+input_user_name+'.txt','r')
            registered_password = account_file.read()
            account_file.close()
            while chance > 0:
                input_password = raw_input('PassWord:')
                if input_password == registered_password:
                    print '\033[32;5m%s login successful @%s\033[0m' %(input_user_name, time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())) )
                    chance = 3
                    break
                else:
                    print 'password incorrect, please try again, you have %s chance left.' % (chance - 1)
                    chance -= 1


        else:
            print 'account %s unregistered! fail to login!' % input_user_name
    # /body of login

    # body of quit
    elif 'q' == choice:
        print '\033[35;1msystem shut down @%s\033[0m' %time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())) 
        break
    # /body of quit

    # body of sub-main
    else:
        print 'invalid code, try again!'
else:
    pass
    
# /body of main    


#print info_interface_login
