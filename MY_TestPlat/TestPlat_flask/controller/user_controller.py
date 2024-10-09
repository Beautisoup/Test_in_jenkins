from importlib.resources import Resource

import requests
from flask import request
from flask_restx import Namespace, fields,Resource

from MY_TestPlat.TestPlat_flask.model.user_model import UserModel
from MY_TestPlat.TestPlat_flask.service.user_service import UserService


user_service = UserService()

user_ns = Namespace('user','用户管理')
'''为什么要继承Resource'''
@user_ns.route('/login')
class login(Resource):
    # post 接口请求体注解，会展示在 Swagger 页面中
    login_post_model = user_ns.model('login_post',{
        'username':fields.String,
        'password':fields.String
    })

    # 为接口添加设置好的注解
    @user_ns.expect(login_post_model)
    def post(self):
        '''登录'''
        data = request.json
        #解包**
        user = UserModel(**data)
        user_password = data.get('password')

        user_result = user_service.get_by_name(user.username)
        if not user_result:
            return {'code': 4001 , 'msg':'user is not register','data':''}
        if not user_result.check_hash_password(user_password):
            #print(user.password,'  ',user.username,'  ',user_result.password,'  ',user_password)
            return {'code': 4002 , 'msg':'password error','data':''}
        #用户存在，生成token
        token = user_service.create_access_token(user)
        print(token)
        if token:
            return {'code': 0 , 'msg':'login success','token':'Bearer'+' '+token,'data':''}
        else:
            return {'code': 4003 , 'msg':'login fail','data':''}

@user_ns.route("/register")
class register(Resource):
    register_post_model = user_ns.model('register_post',{
        'username':fields.String,
        'password':fields.String
    })
    @user_ns.expect(register_post_model)
    def post(self):
        '''注册'''
        data = request.json
        user = UserModel(**data)
        user_username = data.get('username')
        user_password = data.get('password')
        existing_user = user_service.get_by_name(user_username)
        if existing_user:
            return {'code': 4004 , 'msg':'user exists','data':''}
        else:
            user_id = user_service.create(user)
            if user_id:
                return {'code': 0 , 'msg':'register success','data':''}
            else:
                return {'code': 4005 , 'msg':'register fail','data':''}

