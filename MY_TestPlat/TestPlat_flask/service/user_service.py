# 用户 Service
# /user_service.py
from datetime import timedelta
from flask import current_app as app  # 仅保留这一行
from flask_jwt_extended import create_access_token

from MY_TestPlat.TestPlat_flask.dao.user_dao import UserDao
from MY_TestPlat.TestPlat_flask.model.user_model import UserModel
from MY_TestPlat.server import jwt

user_dao = UserDao()


class UserService:

    def get(self, user_id) -> UserModel:
        '''
        通过 ID 查询用户
        '''
        return user_dao.get(user_id)

    def get_by_name(self, user_name):
        '''
        通过姓名查询用户
        '''
        return user_dao.get_by_name(user_name)

    def create(self, user_model: UserModel) -> int:
        '''
        创建用户
        '''
        # 新增前先查询用户是否存在
        user = user_dao.get_by_name(user_model.username)
        if not user:
            # 没有重名，创建用户
            user_dao.create(user_model)
            return user_model.id

    # def create_access_token(self, user_model):
    #     '''
    #     根据用户信息生成 token
    #     '''
    #     # 使用 jwt 生成 token
    #     with app.app_context():
    #         # token = create_access_token(identity=user_model.username, expires_delta=timedelta(days=1))
    #         # identity 是生成 token 的依据，需要 json 格式的可序列化数据
    #         # expires_delta 可以配置 token 的过期时间
    #         token = create_access_token(
    #             identity=user_model.as_dict(),
    #             expires_delta=timedelta(days=1)
    #         )
    #         return token
    #
    # # 配置回调函数中验证数据条件/官方写法
    # @jwt.user_lookup_loader
    # def user_lookup_callback(self, _jwt_header, jwt_data):
    #     # 因为 sub 字段下是请求 body 的内容，所以从 sub 中获取用户名用来查库
    #     # 获取 username
    #     username = jwt_data["sub"]["username"]
    #     # 返回通过 username 查询用户的结果
    #     return self.get_by_name(username)

    def create_access_token(self, user_model):
        '''
        根据用户信息生成 token
        '''
        # token = create_access_token(identity=user_model.username, expires_delta=timedelta(days=1))
        # 直接生成 token，不需要 app_context
        return create_access_token(
            identity=user_model.as_dict(),  # 用户信息序列化为字典
            expires_delta=timedelta(days=1)  # 设置 token 有效期
        )