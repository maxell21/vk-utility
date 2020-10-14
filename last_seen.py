from base import get_login, two_factor_auth
import datetime
import vk_api
import time

platformDict = {1: 'Other app', 2:'iPhone', 3:'iPad', 4:'Android official', 5:'WinPhone', 6:'Win10 official', 7:'Web'}

def dt(u):
	return datetime.datetime.fromtimestamp(u).strftime('%H:%M:%S')

def get_platform(user_data):
	platform_id = user_data[0]['last_seen']['platform']
	return (platformDict[platform_id])

def online(user_data):
	lasttime = user_data[0]['last_seen']['time']
	utctime = dt(lasttime)
	return utctime

def timer(sec, id):
    tmp = 123
    while True:
        user_data = vk.users.get(user_ids = id, fields = 'last_seen')
        utctime = online(user_data)
        platform = get_platform(user_data)

        if utctime != tmp:
            tmp = utctime
            print(utctime, platform)
        time.sleep(sec)


login, password = get_login()
vk_session = vk_api.VkApi(login, password, auth_handler=two_factor_auth)
vk_session.auth()
print('Authorization complete.')
vk = vk_session.get_api()
	
user_id = input('Enter user_id: ')
sec = int(input('Enter time: '))
timer(sec, user_id)
