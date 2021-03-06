from framework.browser_engine import BrowserEngine
from objectpage.mam_login_page import LoginPage
import os.path,csv
from framework.logger import Logger
from objectfunction.personal import Personal
from objectpage.mam_home_page import MAMHomePage

logger = Logger(logger="LoginMAM").getlog()

class LoginMAM(LoginPage):
    def __init__(self,driver):
        self.driver = driver

    def initSetup(self):
        self.browser = BrowserEngine(self)
        self.driver = self.browser.open_browser(self)

    def loginValid(self):
        loginpage = LoginPage(self.driver)
        loginpage.type_user("mam")
        loginpage.type_password("mam")
        # loginpage.type_password("")
        loginpage.login_click()
        # 参数化登陆用户名密码
        # dir = os.path.dirname(os.path.abspath('.')) + '/parameters/'
        # login_pp = dir + 'login_parameter.csv'
        #读取csv并将内容写到字典中
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
        #读取每组用户名密码，完成打开个人中心，完成任务分配操作。并点击退出这一过程
        #后续考虑增加多进程处理
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
        #主页打开个人中心的方法
        #     hompage = MAMHomePage(self.driver)
        #     hompage.personal_click()
        #个人中心相关操作
        #     personal = Personal(self.driver)
        #     personal.CatalogAssignTask()
        #完成以上操作后退出系统
        #     loginpage.logout_element()
        #     loginpage.login_sleep(1)
        #     i += 1



