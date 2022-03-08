# coding:utf-8

from selenium.webdriver.common.keys import Keys
from selenium.webdriver import Remote
import time

# 定义node_hub与浏览器对应关系
nodes = {
    'http://127.0.0.1:5555/wd/hub': 'chrome',
    'http://127.0.0.1:5556/wd/hub': 'internet explorer',
    'http://127.0.0.1:5557/wd/hub': 'firefox'
}

# 通过不同的浏览器执行测试脚本
for host, browser in nodes.items():
    print(host, browser)
    # 调用remote方法
    driver = Remote(command_executor=host,
                    desired_capabilities={'platform': 'ANY', 'browserName': browser, 'version': '', 'javascriptEnabled': True,'ignore_zoom_level':True})

    # 打开百度首页并搜索词语，最后判断搜索跳转页面标题是否含有搜索词
    # wd = 'lovesoo'
    driver.get('https://www.baidu.com')
    driver.implicitly_wait(30)
    time.sleep(2)
    # driver.find_element_by_id("kw").send_keys("lovesoo\n")
    driver.find_element_by_id("kw").send_keys("lovesoo")
    time.sleep(2)
    driver.find_element_by_id("su").send_keys(Keys.ENTER)
    time.sleep(8)
    print(driver.title)
    # assert 'lovesoo' in driver.title, '{0} not in {1}'.format('lovesoo', driver.title.encode('utf-8'))
    assert 'lovesoo' in driver.title
    driver.quit()