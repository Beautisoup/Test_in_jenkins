from flask import request
from flask_jwt_extended import jwt_required
from flask_restx import Namespace, Resource, fields

from MY_TestPlat.TestPlat_flask.service.record_service import RecordService
from MY_TestPlat.server import api

record_ns = Namespace("record", description="测试记录管理")

record_service = RecordService()


@record_ns.route("")
class RecordController(Resource):
    # 鉴权操作
    decorators = [jwt_required()]
    record_get_parser = api.parser()
    record_get_parser.add_argument("plan_id", type=int, location="args")
    record_get_parser.add_argument('Authorization', type=str, location="headers")

    @record_ns.expect(record_get_parser)
    # @jwt_required()
    def get(self):
        """
        测试记录的查找
        :return:
        """
        plan_id = request.args.get("plan_id")
        if plan_id:
            # 如有有id则进行数据查找
            data = record_service.list_by_plan(plan_id)
            if data:
                # 如果查到数据，则返回给前端
                datas = [_.as_dict() for _ in data]
                return {"code": 0, "msg": "get record success", "data": datas}
            else:
                # 如果没有数据，则返回数据已存在
                return {"code": 40004, "msg": "record is not exists"}
        else:
            # 如果没有id,则返回全部数据
            datas = [build.as_dict() for build in record_service.list()]
            return {"code": 0, "msg": "get records success", "data": datas}

    record_post_model = record_ns.model("build_post_model", {
        "plan_id": fields.Integer
    })
    record_post_parser = api.parser()
    record_post_parser.add_argument('Authorization', type=str, location="headers")

    @record_ns.expect(record_post_model, record_post_parser)
    def post(self):
        """
        测试记录的新增
        :return:
        """
        data = request.json
        # 新增
        record_id = record_service.create(data.get("plan_id"))
        if record_id:
            # 存在id,则证明新增成功了
            return {"code": 0, "msg": f"record add success", "data": {"record_id": record_id}}
        else:
            return {"code": 40001, "msg": "record is exists"}
