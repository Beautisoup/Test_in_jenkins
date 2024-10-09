from urllib.parse import urljoin

import pytest
import requests

base_url = 'http://127.0.0.1:5055/testcase'
user_list = [
    {
        'username': 'AA',
        'password': '123456'
    },
    {
        'username': 'BB',
        'password': '123456'
    },
    {
        'username': 'CC',
        'password': '123456'
    }
]
class TestUserController:
    @pytest.mark.parametrize('user', user_list)
    def test_login(self,user):
        #拼接url
        url = urljoin(base_url, '/user/login')
        #取出用户名,密码
        username= user.get('username')
        password= user.get('password')
        data = {
            'username': username,
            'password': password
        }
        #发送请求
        response = requests.post(url, json=data)
        print(response.json())
        the_json = response.json()
        assert the_json['code'] == 0,the_json['msg']=='login success'



    '''
     pytest -sv test_user_controller.py --alluredir=allure_data
     
     allure serve allure_data

     allure generate allure_data -o allure_report --clean
     allure open allure_report
    '''