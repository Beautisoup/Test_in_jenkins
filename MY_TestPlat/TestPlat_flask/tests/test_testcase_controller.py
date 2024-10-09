import requests
from _pytest.fixtures import fixture

baseurl = "http://127.0.0.1:5055/testcase"
@fixture(scope='class')
def init_login_token():
    url = "http://127.0.0.1:5055/user/login"
    user = {
        "username": "AA",
        "password": "123456"
    }
    r = requests.post(url, json=user)
    token = r.json()['token']
    #print(token)
    # JWT添加token到请求头内的操作
    # 返回一个字典，包含 headers 和其他可能需要的初始化数据
    data = {
        'id': 112,
        'name': 'test_post2',
        'step': '接口测试',
        'method': 'pytest',
        'remark': '使用request进行接口测试'
    }
    return {'headers': {'Authorization': token}, 'data': data}

class TestcaseController:
    #因为所有接口都需要登陆后获取token,所以在这里获取token
    #新增
    def test_post(self,init_login_token):
        data = init_login_token['data']
        headers = init_login_token['headers']
        #print(headers)
        r = requests.post(baseurl, json=data,headers=headers)
        print(r.json())

    def test_put(self,init_login_token):
        data = init_login_token['data']
        headers = init_login_token['headers']
        r = requests.put(baseurl, json=data,headers=headers)
        print(r.json())
        assert r.json()['msg'] == 'update testcase success'

    def test_delete(self,init_login_token):
        id = init_login_token['data']['id']
        headers = init_login_token['headers']
        r = requests.delete(baseurl,json={'id': id},headers=headers)
        print(r.json())
        assert r.json()['msg'] == 'delete testcase success'



