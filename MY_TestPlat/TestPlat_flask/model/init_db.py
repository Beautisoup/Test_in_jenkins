# model/init_db.py

"""
初始化数据库表文件
"""
from MY_TestPlat.server import Base, engine
'''
中间表不用导入 #from MY_TestPlat.TestPlat_flask.model.testcase_plan_rel import testcase_plan_rel
'''


if __name__ == '__main__':
    # 删除所有数据
    # Base.metadata.drop_all(bind=engine)
    # 创建表，需要传入创建连接的对象
    Base.metadata.create_all(bind=engine)