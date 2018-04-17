# -*- coding:utf-8 -*-
from page.base_page import BasePage


class IndexPage(BasePage):
    '''
        用来别对用户昵称
    '''
    url = '/index'
    def get_user_name(self):
        # 获取用户昵称
        name = self.find_element_by_css('.yk-name').text
        return name