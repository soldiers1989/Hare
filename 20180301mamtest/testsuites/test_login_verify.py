
from objectpage.mam_login_page import LoginPage
import unittest
from framework.browser_engine import BrowserEngine
from framework.logger import Logger
import csv,os.path

logger = Logger(logger="login").getlog()

class login(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.browser = BrowserEngine(cls)
        cls.driver = cls.browser.open_browser(cls)
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    # 该方法用来读取csv文件中的内容
    # 可以提取为一个常用的参数化类出来，该部分代码的完整实现被写到了function文件夹里的login里了。
    def open_csv(self,colnameindex=0,by_index=0):

        dir = os.path.dirname(os.path.abspath('.')) + '/parameters/'
        login_pp = dir + 'login_parameter.csv'

        login_parameter = csv.DictReader(open(login_pp, 'r'))
        dict_data = []
        # 格式化字典内容
        for lines in login_parameter:
            if login_parameter.line_num == 1:
                continue
            else:
                dict_data.append(lines)

        row_num = len(dict_data)
        print(row_num)
        i = 0
        # 获取到所有的字典内容
        while(i < row_num):
            print("This is -->"+str(i)+"-->row-->"+str(dict_data[i]))
            i += 1

    def test_login(self):
        # 参数化登陆用户名密码
        loginpage = LoginPage(self.driver)
        # dir = os.path.dirname(os.path.abspath('.')) + '/parameters/'
        # login_pp = dir + 'login_parameter.csv'
        #获取csv文件中的数据，并保存成字典
        # login_parameter = csv.DictReader(open(login_pp, 'r'))
        # dict_data = []

        #格式化字典内容
        # for lines in login_parameter:
        #     if login_parameter.line_num == 1:
        #         continue
        #     else:
        #         dict_data.append(lines)
        #
        # row_num = len(dict_data)
        # print(row_num)
        # 对csv文件中所有行，用户名密码进行读取登陆，每组用户名都完成登陆到个人中心的分配操作
        # i = 0
        # while (i < row_num):
        #     loginpage.type_user(dict_data[i]['\ufeffUSERID'])
        #     loginpage.type_password(dict_data[i]['PASSWORD'])
        #     loginpage.login_click()
        #     loginpage.login_sleep(1)
        #     try:
        #         assert "首页" in loginpage.get_page_title()
        #         loginpage.get_windows_img()
        #         logger.info("Open homepage is OK!")
        #     except Exception as e:
        #         logger.error("sorry!Open Homepage fail %s" % e)
        #     loginpage.logout_element()
        #     loginpage.login_sleep(1)
        #     i += 1

        loginpage.login_click()
        loginpage.login_sleep(1)

if __name__ == '__main__':
    unittest.main
