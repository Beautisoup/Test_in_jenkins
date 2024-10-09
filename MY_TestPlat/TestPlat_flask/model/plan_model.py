# 测试计划模型
# model/plan_model.py

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from MY_TestPlat.TestPlat_flask.model.testcase_plan_rel import testcase_plan_rel
from MY_TestPlat.server import Base

class PlanModel(Base):

    __tablename__ = "plan"

    # 测试计划 ID
    id = Column(Integer, primary_key=True)
    # 测试计划名称
    name = Column(String(80), nullable=False, unique=True)
    # 测试用例列表
    testcases = relationship("TestcaseModel", secondary=testcase_plan_rel, backref='plan')

    def __repr__(self):
        # 数据库的 魔法方法 直观展示数据
        '''[<User "xxxx">,<User "yyyy">]'''
        return '<Plan %r>' % self.name

    def as_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "testcases": [testcase.as_dict() for testcase in self.testcases],
        }