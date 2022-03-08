from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import unittest


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get('https://hotels.ctrip.com/')
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        sleep(2)

    def tearDown(self) -> None:
        pass



    def test_01(self):
        try:
            # 1.使用QQ登录
            self.driver.find_element_by_xpath('//*[@id="nav-bar-set-login-person-text"]/span').click()

            sleep(1)
            self.driver.find_element_by_xpath('//*[@id="normalview"]/p/input').click()

            sleep(1)
            self.driver.find_element_by_xpath('//*[@id="loginbanner"]/div[2]/a[2]').click()

            sleep(1)
            self.driver.switch_to.window(self.driver.window_handles[-1])

            sleep(1)
            iframe = self.driver.find_element_by_xpath('//*[@id="ptlogin_iframe"]')
            self.driver.switch_to.frame(iframe)

            sleep(1)
            self.driver.find_element_by_id('img_out_1476115944').click()

            sleep(5)
            self.driver.switch_to.window(self.driver.window_handles[0])
            dy_01 = self.driver.find_element_by_xpath('//*[@id="nav-bar-set-myctrip-name"]/a/span/span').text
            self.assertEqual('尊敬的白银贵宾', dy_01)

            # 2.点击首页 - 火车

            self.driver.find_element_by_xpath('//*[@id="nav_trains"]').click()
            sleep(2)
            # 3.输入出发城市为南京
            self.driver.find_element_by_xpath('//*[@id="label-departStation"]').click()
            self.driver.find_element_by_xpath('//*[@id="label-departStation"]').send_keys(Keys.BACKSPACE)
            self.driver.find_element_by_xpath('//*[@id="label-departStation"]').send_keys(Keys.BACKSPACE)
            self.driver.find_element_by_xpath('//*[@id="label-departStation"]').send_keys('南京')

            # 4.输入到达城市为北京
            self.driver.find_element_by_xpath('//*[@id="label-arriveStation"]').click()
            self.driver.find_element_by_xpath('//*[@id="label-arriveStation"]').send_keys(Keys.BACKSPACE)
            self.driver.find_element_by_xpath('//*[@id="label-arriveStation"]').send_keys(Keys.BACKSPACE)
            self.driver.find_element_by_xpath('//*[@id="label-arriveStation"]').send_keys('北京')

            sleep(2)
            # 5.点击搜索
            self.driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[1]/div[2]/div[2]/div/div[1]').click()
            sleep(1)
            self.driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[1]/div[2]/button').click()

            # 6.选择合适的时间，点击订
            self.driver.find_element_by_xpath('//*[@id="trainlistitem0"]/div/button').click()

            sleep(2)
            # 7.选择座次，点击预定
            self.driver.find_element_by_xpath('//*[@id="__next"]/div/div[3]/div[1]/section/div[2]/ul/li[1]/button').click()

            sleep(2)
        except:
            print('BUG')

    def test_02(self):
        try:
            self.driver.get('https://hotels.ctrip.com/')

            # 1.使用QQ登录
            self.driver.find_element_by_xpath('//*[@id="nav-bar-set-login-person-text"]/span').click()

            sleep(1)
            self.driver.find_element_by_xpath('//*[@id="normalview"]/p/input').click()

            sleep(1)
            self.driver.find_element_by_xpath('//*[@id="loginbanner"]/div[2]/a[2]').click()

            sleep(1)
            self.driver.switch_to.window(self.driver.window_handles[-1])

            sleep(1)
            iframe = self.driver.find_element_by_xpath('//*[@id="ptlogin_iframe"]')
            self.driver.switch_to.frame(iframe)

            sleep(1)
            self.driver.find_element_by_id('img_out_1476115944').click()

            sleep(5)
            self.driver.switch_to.window(self.driver.window_handles[0])
            dy_01 = self.driver.find_element_by_xpath('//*[@id="nav-bar-set-myctrip-name"]/a/span/span').text
            self.assertNotEqual('尊敬的白银', dy_01)

            sleep(2)

            self.driver.refresh()

            sleep(2)

            # 2.点击首页 - 酒店
            self.driver.find_element_by_link_text('酒店').click()

            sleep(1)
            # 3.填写目的地为北京
            xf_01 = self.driver.find_element_by_xpath('//*[@id="hotels-destination"]')
            ActionChains(self.driver).move_to_element(xf_01).perform()

            sleep(1)

            for i in range(3):
                self.driver.find_element_by_xpath('//*[@id="hotels-destination"]').click()

            sleep(1)

            self.driver.find_element_by_xpath('//*[@id="hotels-destination"]').send_keys(Keys.BACKSPACE)

            sleep(1)

            self.driver.find_element_by_xpath('//*[@id="hotels-destination"]').send_keys('北京')

            sleep(2)
            # 4.点击搜索
            self.driver.find_element_by_xpath('//*[@id="ibu_hotel_container"]/div[1]/div[1]/div[3]/div/div/ul/li[5]/button/i').click()

            sleep(2)
        except:
            print('BUG')

    def test_03(self):
        try:
            self.driver.get('https://hotels.ctrip.com/')
            # 1.使用QQ登录

            self.driver.find_element_by_xpath('//*[@id="nav-bar-set-login-person-text"]/span').click()

            sleep(1)
            self.driver.find_element_by_xpath('//*[@id="normalview"]/p/input').click()

            sleep(1)
            self.driver.find_element_by_xpath('//*[@id="loginbanner"]/div[2]/a[2]').click()

            sleep(1)
            self.driver.switch_to.window(self.driver.window_handles[-1])

            sleep(1)
            iframe = self.driver.find_element_by_xpath('//*[@id="ptlogin_iframe"]')
            self.driver.switch_to.frame(iframe)

            sleep(1)

            self.driver.find_element_by_id('img_out_1476115944').click()

            sleep(5)

            self.driver.switch_to.window(self.driver.window_handles[0])
            dy_01 = self.driver.find_element_by_xpath('//*[@id="nav-bar-set-myctrip-name"]/a/span/span').text
            self.assertIn('尊敬的白银贵宾', dy_01)

            sleep(3)

            # 2.点击首页 - 消息
            self.driver.find_element_by_xpath('//*[@id="nav-bar-set-msgnum"]').click()

            # 3.进入消息列表并获取所有信息
            data_xx = self.driver.find_element_by_xpath('//*[@id="__next"]/div/div[2]/div[2]/table/tbody').text
            print(data_xx)
        except:
            print('BUG')

    def test_04(self):
        try:
            self.driver.get('https://hotels.ctrip.com/')

            # 1.使用QQ登录

            self.driver.find_element_by_xpath('//*[@id="nav-bar-set-login-person-text"]/span').click()

            sleep(1)

            self.driver.find_element_by_xpath('//*[@id="normalview"]/p/input').click()

            sleep(1)

            self.driver.find_element_by_xpath('//*[@id="loginbanner"]/div[2]/a[2]').click()

            sleep(1)

            self.driver.switch_to.window(self.driver.window_handles[-1])

            sleep(1)

            iframe = self.driver.find_element_by_xpath('//*[@id="ptlogin_iframe"]')
            self.driver.switch_to.frame(iframe)

            sleep(1)

            self.driver.find_element_by_id('img_out_1476115944').click()

            sleep(5)

            self.driver.switch_to.window(self.driver.window_handles[0])
            dy_01 = self.driver.find_element_by_xpath('//*[@id="nav-bar-set-myctrip-name"]/a/span/span').text
            self.assertEqual('尊敬的白银贵宾', dy_01)

            # self.driver.find_element_by_xpath('//*[@id="nav-bar-set-myctrip-name"]/a/span/span').send_keys(Keys.F5)

            # 2.点击首页 - 个人中心
            sleep(2)

            self.driver.find_element_by_xpath('//*[@id="nav-bar-set-myctrip-name"]/a/span/span').click()

            sleep(2)
            # 3.点击个人中心 - 个人中心

            self.driver.find_element_by_xpath('//*[@id="sideNav"]/dl[10]/dt/a/span').click()

            sleep(2)
            # 4.点击个人信息并获取
            self.driver.find_element_by_xpath('//*[@id="info_myaccount"]/span').click()

            data_grxx = self.driver.find_element_by_xpath('//*[@id="info_display_id"]/ul[1]').text
            print(data_grxx)

            sleep(2)

            self.driver.quit()
        except:
            print('BUG')



if __name__ == '__main__':
    # unittest.main()

    runner = unittest.TextTestRunner()
    loader = unittest.TestLoader()
    load = loader.discover('.', 'test_run.py')
    runner.run(load)




















