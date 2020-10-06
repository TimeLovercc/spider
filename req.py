from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time

# dcap = dict(DesiredCapabilities.PHANTOMJS)
# dcap["phantomjs.page.settings.userAgent"] = (
# "Mozilla/5.0 (Linux; Android 5.1.1; Nexus 6 Build/LYZ28E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.23 Mobile Safari/537.36"
# )

# # driver = webdriver.PhantomJS(desired_capabilities=dcap)
# driver = webdriver.PhantomJS()


# print(driver.get_cookies())
# driver.add_cookie({'name':'name', 'value':'value'})
# time.sleep(30)

url = 'http://106.15.250.17:6888/wd/hub'
descaps = {'browserName': 'chrome', 'loggingPrefs': {'performance': 'INFO'}}
driver = webdriver.Remote(command_executor=url, desired_capabilities=descaps)
driver.get('https://www.zhihu.com/search?q=%E7%94%B5%E5%AD%90%E7%A7%91%E6%8A%80%E5%A4%A7%E5%AD%A6&type=content')

# driver.get('https://www.zhihu.com/api/v4/search_v3?t=general&q=%E7%94%B5%E5%AD%90%E7%A7%91%E6%8A%80%E5%A4%A7%E5%AD%A6&correction=1&offset=0&limit=20&lc_idx=0&show_all_topics=0')

# time.sleep(3)


driver.get_screenshot_as_file('01.png')
driver.quit()

