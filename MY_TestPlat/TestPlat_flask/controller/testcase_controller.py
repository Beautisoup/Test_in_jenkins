from flask import request
from flask_jwt_extended import jwt_required
from flask_restx import Namespace, Resource, fields

from MY_TestPlat.TestPlat_flask.model.testcase_model import TestcaseModel
from MY_TestPlat.TestPlat_flask.service.testcase_service import TestcaseService
from MY_TestPlat.server import api

testcase_service = TestcaseService()
#定义命名空间
testcase_ns = Namespace('Testcase', '用例管理')
'''severe层里的url是第一层，@testcase_ns.route('')是第二层'''
#定义子路由
@testcase_ns.route('')
class TestCase(Resource):
    #增加鉴权操作，这是官方写法
    decorators = [jwt_required()]
    #定义测试用例的增删改查操作

    # 类内定义parser解析器对象
    testcase_get_parser = api.parser()
    # 添加测试参数
    testcase_get_parser.add_argument('id', type=int, location='args')
    testcase_get_parser.add_argument('Authorization', type=str, location='headers')
    @testcase_ns.expect(testcase_get_parser)
    def get(self):
        '''测试用例查找'''
        # 获取请求参数
        data = request.args
        case_id = data.get("id")
        # 如果有id则进行数据查找
        if case_id:
            testcase = testcase_service.get(int(case_id))
            # 如果查询到结果
            if testcase:
                datas = [testcase.as_dict()]
                return {"code": 0, "msg": "get data success", "data": datas}
            else:
                # 如果没有数据，则返回数据已存在
                return {"code": 40004, "msg": "data is not exists",'data':''}
        else:
            # 如果没有id,则返回全部数据
            datas = [testcase.as_dict() for testcase in testcase_service.list()]
            return {"code": 0, "msg": "get data success", "data": datas}

    # post 接口请求体注解，会展示在 Swagger 页面中
    testcase_post_model = testcase_ns.model('testcase_post_model', {
        'name': fields.String,
        'step': fields.String,
        'method': fields.String,
        'remark': fields.String
    })
    # 测试用例管理 post 接口请求参数注解因为有Authorization所以也有头
    testcase_post_parser = api.parser()
    testcase_post_parser.add_argument('Authorization', required=True, type=str, location='headers')

    # 为方法添加解释器和参数
    @testcase_ns.expect(testcase_post_model,testcase_post_parser)
    def post(self):
        '''用例新增'''
        # 获取请求体
        data = request.json
        # 构造测试用例对象
        testcase = TestcaseModel(**data)
        # 新增测试用例
        id = testcase_service.create(testcase)
        if id:
            return {'code':0,'msg':'create testcase success','data':testcase.as_dict()}
        else:
            return {'code':4001,'msg':'testcase is exists','data':''}

    # put 接口请求体注解，会展示在 Swagger 页面中
    testcase_put_model = testcase_ns.model('testcase_put_model',{
        'id': fields.String,
        'name': fields.String,
        'step': fields.String,
        'method': fields.String,
        'remark': fields.String
    })
    testcase_put_parser = api.parser()
    testcase_put_parser.add_argument('Authorization', required=True, type=str, location='headers')

    # 为方法添加解释器和参数
    @testcase_ns.expect(testcase_put_model,testcase_put_parser)
    def put(self):
        '''测试用例更新'''
        data = request.json
        testcase_id = data.get("id")
        testcase_name = data.get("name")
        testcase = TestcaseModel(**data)

        # 查询数据库中的测试用例
        testcase_in_db = testcase_service.get(testcase_id)

        # 检查 id 是否存在
        if not testcase_in_db:
            return {'code': 4001, 'msg': 'testcase not found'}

        # 检查请求中的 name 与数据库中的 name 是否匹配
        if testcase_in_db.name != testcase_name:
            return {'code': 4001, 'msg': 'id and name do not match the database'}
        id = testcase_service.update(testcase)
        if id:
            return {'code':0,'msg':'update testcase success','data':testcase.as_dict(),'testcase_in_db.name':testcase_in_db.name}
        else:
            return {'code':4001,'msg':'update failed'}

    testcase_delete_parser = api.parser()
    testcase_delete_parser.add_argument('Authorization', required=True, type=str, location='headers')
    testcase_delete_parser.add_argument('id', required=True, type=int, location='json')
    '''从哪里得来的delete接口id参数来自json'''
    @testcase_ns.expect(testcase_delete_parser)
    def delete(self):
        data = request.json
        id = data.get('id')
        if id:
            idd = testcase_service.delete(id)
            if idd:
                return {'code':0,'msg':'delete testcase success','id':idd}
            else:
                return {'code':4001,'msg':'delete failed'}