import time
from selenium import webdriver

# from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
url = 'http://mail.163.com/'
browser.get(url)
time.sleep(3)

browser.maximize_window()  # 打开网页窗口

time.sleep(5)

browser.switch_to.frame(0)  # 找到邮箱账号登录框对应的iframe,由于网页中iframe的id是动态的，所以不能用id寻找

email = browser.find_element_by_name('email')  # 找到邮箱账号输入框

email.send_keys('18811704711@163.com')  # 将自己的邮箱地址输入到邮箱账号框中

password = browser.find_element_by_name('password')  # 找到密码输入框

password.send_keys('!w922169')  # 输入自己的邮箱密码

login_em = browser.find_element_by_id('dologin')  # 找到登陆按钮

login_em.click()  # 点击登陆按钮

time.sleep(10)
