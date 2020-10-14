import getpass

def two_factor_auth():
    check_code = getpass.getpass('Two factor auth code: ')
    rem = True
    return  check_code, re

def get_login():
	ans = input('Login as new user? (y/n) ').lower()
	
	if ans == 'y' or ans == 'yes' or ans == 'д' or ans == 'да':
		login = input('enter login: ')
		password = getpass.getpass('enter password: ')
	
	else:
		from config import login, password
	
	return login, password