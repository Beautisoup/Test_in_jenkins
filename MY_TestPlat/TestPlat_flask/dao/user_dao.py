# 用户 Dao
# dao/user_dao.py

from MY_TestPlat.TestPlat_flask.model.user_model import UserModel
from MY_TestPlat.server import db_session

class UserDao:
    def get(self,user_id:int) -> UserModel:
        return db_session.query(UserModel).filter_by(id = user_id).first()

    def get_by_name(self,name_name:str) -> UserModel:
        return db_session.query(UserModel).filter_by(username = name_name).first()

    def create(self,usermodel:UserModel):
        db_session.add(usermodel)
        db_session.commit()
        return usermodel.id


