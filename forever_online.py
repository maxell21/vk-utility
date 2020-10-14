from base import get_login, two_factor_auth
import vk_api
import time

login, password = get_login()
vk_session = vk_api.VkApi(login, password, auth_handler=two_factor_auth)
vk_session.auth()
vk = vk_session.get_api()		

while True:
	exit = vk.account.setOnline()
	print('online')
	time.sleep(290)
