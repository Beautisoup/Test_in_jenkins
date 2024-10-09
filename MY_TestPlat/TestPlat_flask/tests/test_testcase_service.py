from MY_TestPlat.TestPlat_flask.dao.testcase_dao import TestcaseDao
from MY_TestPlat.TestPlat_flask.model.testcase_model import TestcaseModel
from MY_TestPlat.TestPlat_flask.service.testcase_service import TestcaseService

case = TestcaseService()

class Test_Case_Service:
    def test_create(self):
        test_case1 = TestcaseModel(id=1, name='test1',step='no',method='no',remark='no')
        #case = TestcaseService()
        case.create(test_case1)
        assert case

    def test_create2(self, mocker):
        # 创建一个假测试用例
        test_case1 = TestcaseModel(id=1, name='test1', step='no', method='no', remark='no')

        # 模拟 TestcaseDao.get_by_name 方法，确保返回 None，这样服务层会尝试创建测试用例
        mocker.patch.object(TestcaseDao, 'get_by_name', return_value=None)

        # 模拟 TestcaseDao.create 方法，确保不会实际调用数据库
        mocker.patch.object(TestcaseDao, 'create', return_value=1)  # 假设返回 id 为 1

        # 实例化服务
        service = TestcaseService()

        # 调用服务的 create 方法
        result = service.create(test_case1)

        # 验证结果
        assert result == 1

    def test_update(self):
         testcase2 = TestcaseModel(id=1, name='test1', step='yyyyy', method='yyyy0', remark='no00')
         case.update(testcase2)
         resule = case.get(1).as_dict()
         print(resule)
         assert resule['step'] == 'yyyyy'

    # def test_list(self):
    #     assert False

    def test_get(self):
        case.get(1)
        result = case.get(1).as_dict()
        print(result)
        assert result['id'] == 1

    def test_delete(self):
        test_id = 1
        case.delete(test_id)
        assert case