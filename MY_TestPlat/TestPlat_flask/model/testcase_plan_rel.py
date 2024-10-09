# 测试用例与测试计划中间表
# testcase_plan_rel.py

from sqlalchemy import Table, Column, Integer, ForeignKey
from MY_TestPlat.server import Base

# 中间表
# 中间表表名
# 测试用例的外键
# 计划的外键

testcase_plan_rel = Table(
    "testcase_plan_rel", # 表名
    Base.metadata,   # 表继承的类
    # 参数一： 表名_id， 参数二：整型，参数3： 外键字符串('表名.id'， 参数4： 是否为主键)
    Column('testcase_id', Integer, ForeignKey('testcase.id', ondelete='CASCADE'), primary_key=True),
    Column('plan_id', Integer, ForeignKey('plan.id', ondelete='CASCADE'), primary_key=True)
)