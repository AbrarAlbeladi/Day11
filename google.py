
from helium.api import *
start_chrome("http://www.bing.com")
write("cloudsystems.sa")
press(ENTER)
click("Cloud Systems")
click("Contact Us")
if 'Contact Us' in get_driver().title:
	print('Test passed!')
else:
	print('Test failed :(')
kill_browser()
