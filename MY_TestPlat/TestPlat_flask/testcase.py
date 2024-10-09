from unittest import TestCase
from flask import Flask, request
from flask_restx import Api, Namespace, Resource
from pymysql import Connect
app = Flask(__name__)



api = Api(app)
db_connect = Connect(
    host='localhost',
    port=3306,
    user='root',
    password='123456',
    database='tps',
    charset='utf8'
)
# 1、定义 namespace（不同的路由可以定义不同的 namespace ）
testcase = Namespace('testcase',description='testcase curd')

# 定义类，继承自 Resource
class Testcase(Resource):
    get_parser = api.parser()
    # 添加测试参数
    # location的值对应request对象的一些属性
    get_parser.add_argument('id', type=int, location='args')
    api.expect(get_parser)
    def get(self):
        case_id = request.args.get('id')
        if case_id :
            case_data = TestCase.query.filter_by(id=case_id).first()
            if case_data:
                datas = [{
                    'id': case_id,
                    'title' : case_data.title,
                    'remark' : case_data.remark,
                }]
            else:
                datas = []
        else:
            case_datas = TestCase.query.all()
            datas = [{"id": case_data.id, "title": case_data.title, "remark": case_data.remark} for case_data in
                     case_datas]

        return datas

    post_parser = api.parser()
    # 添加测试参数
    # location的值对应request对象的一些属性
    post_parser.add_argument('id', type=int, location='json', required=True)
    post_parser.add_argument('title', type=str, location='json', required=True)
    post_parser.add_argument('remark', type=str, location='json')

    api.expect(post_parser)
    def post(self):
        '''新增接口'''
        #获取请求数据
        case_data = request.json
        case_id = case_data['id']
        #查询数据库看是否有记录
        exists = TestCase.query.filter(TestCase.id == case_id).scalar()
        if exists:
            return {"code": 0, "msg": "user, post success"}
        if not exists:
            return {"code": 1, "msg": "user, post fail"}

    def put(self):
        return {"code": 0, "msg": "user, put success"}

    def delete(self):
        return {"code": 0, "msg": "user, delete success"}
# 3、通过 api实例 将预先定义的 namespace 与 路由绑定
api.add_resource(Testcase, '/testcase')

if __name__ == '__main__':
    app.run(debug=True)

