# 测试计划管理接口
# controller/plan_controller.py

from flask import request
from flask_jwt_extended import jwt_required
from flask_restx import Namespace, Resource, fields

from MY_TestPlat.TestPlat_flask.model.plan_model import PlanModel
from MY_TestPlat.TestPlat_flask.service.plan_service import PlanService
from MY_TestPlat.server import api

plan_ns = Namespace("plan", description="测试计划管理")

plan_service = PlanService()


@plan_ns.route("")
class PlanController(Resource):
    # 鉴权操作
    decorators = [jwt_required()]

    plan_get_parser = api.parser()
    plan_get_parser.add_argument('id', type=int, location="args")
    plan_get_parser.add_argument('Authorization', type=str, location="headers")

    @plan_ns.expect(plan_get_parser)
    def get(self):
        '''
        查询测试计划
        '''
        # 获取请求参数
        id = request.args.get("id")
        # 如果请求参数中存在 id
        if id:
            # 根据 id 查询测试计划
            data = plan_service.get(id)
            # 如果测试计划存在
            if data:
                # 将查询结果返回
                datas = [data.as_dict()]
                return {"code": 0, "msg": "get plan success", "data": datas}
            else:
                # 如果测试计划不存在，返回提示信息
                return {"code": 40004, "msg": "plan is not exists"}
        else:
            # 如果参数中不包含 id，则返回全部测试计划
            datas = [p.as_dict() for p in plan_service.list()]
            return {"code": 0, "msg": "get plans success", "data": datas}

    plan_post_parser = api.parser()
    plan_post_parser.add_argument('Authorization', type=str, location="headers")
    plan_post_model = plan_ns.model("plan_post_model", {
        "name": fields.String,
        "testcase_ids": fields.List(fields.Integer)
    })

    @plan_ns.expect(plan_post_model, plan_post_parser)
    def post(self):
        '''
        新增测试计划
        '''
        data = request.json
        # data -> {name=1, testcase_ids=[2,3,4,5,6]}
        testcase_id_list = data.pop("testcase_ids")
        plan = PlanModel(**data)
        # 新增
        plan_id = plan_service.create(plan, testcase_id_list)
        if plan_id:
            # 存在id,则证明新增成功了
            return {"code": 0, "msg": f"add plan success", "data": {"plan_id": plan_id}}
        else:
            return {"code": 40001, "msg": "plan is exists"}

    plan_delete_parser = api.parser()
    plan_delete_parser.add_argument("id", type=int, location="json", required=True)
    plan_delete_parser.add_argument('Authorization', type=str, location="headers")

    @plan_ns.expect(plan_delete_parser)
    def delete(self):
        """
        测试计划的删除
        :return:
        """
        # data ==> {"id": 1}
        data = request.json
        # 删除
        plan_id = plan_service.delete(data.get("id"))
        if plan_id:
            # 存在测试用例id,则证明用例修改成功了
            return {"code": 0, "msg": f"plan delete success", "data":{"plan_id": plan_id}}
        else:
            return {"code": 40001, "msg": "delete plan fail"}