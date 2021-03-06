
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

        loginpage = LoginPage(self.driver)

        loginpage.type_user("mam")
        loginpage.type_password("qwe123!@#2018")
        loginpage.login_click()
        loginpage.login_sleep(10)

        try:
            assert "首页" in loginpage.get_page_title()
            loginpage.get_windows_img()
            logger.info("Open homepage is OK!")
        except Exception as e:
            logger.error("sorry!Open Homepage fail %s" % e)


if __name__ == '__main__':
    unittest.main
