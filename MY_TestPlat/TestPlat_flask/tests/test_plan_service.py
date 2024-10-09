from MY_TestPlat.TestPlat_flask.model.plan_model import PlanModel
from MY_TestPlat.TestPlat_flask.model.testcase_model import TestcaseModel
from MY_TestPlat.TestPlat_flask.service.plan_service import PlanService
from MY_TestPlat.TestPlat_flask.service.testcase_service import TestcaseService

case = TestcaseService()
plan = PlanService()
class Test_Plan_Service:
    def test_get(self):
        assert False

    def test_get_by_name(self):
        assert False

    def test_list(self):
        assert False

    def test_create(self):
        test_case = TestcaseModel(id=111, name='test1',step='no',method='pytest',remark='no')
        case.create(test_case)
        testplan = PlanModel(id = 1, name= 'plan1')
        plan.create(testplan,[111])
        assert plan

    def test_delete(self):
        assert False
