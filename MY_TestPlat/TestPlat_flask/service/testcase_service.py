# 测试用例 Service
# service/testcase_service.py

from typing import List

from MY_TestPlat.TestPlat_flask.dao.testcase_dao import TestcaseDao
from MY_TestPlat.TestPlat_flask.model.testcase_model import TestcaseModel

# 实例化测试用例实体类
testcase_dao = TestcaseDao()


class TestcaseService:
    def create(self, testcase_model: TestcaseModel) -> int:
        """
        创建用例
        """
        #首先校验名称是否是不存在的
        result = testcase_dao.get_by_name(testcase_model.name)
        #不存在则创建用例
        if not result:
            return testcase_dao.create(testcase_model)

    def update(self, testcase_model: TestcaseModel) -> int:
        """
        更新用例
        """
        if testcase_dao.get_by_name(testcase_model.name):
            testcase_dao.update(testcase_model)
        return testcase_model.id

    def delete(self, testcase_id: int) -> int:
        """
        删除用例
        """
        if self.get(testcase_id):
            return testcase_dao.delete(testcase_id)

    def list(self) -> List[TestcaseModel]:
        """
        获取全部用例
        """
        return testcase_dao.list()

    def get(self, testcase_id):
        """
        获取某个测试用例
        """
        return testcase_dao.get(testcase_id)