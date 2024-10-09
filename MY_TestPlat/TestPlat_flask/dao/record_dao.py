# 测试记录 Dao
# dao/record_dao.py

from MY_TestPlat.TestPlat_flask.model.record_model import RecordModel
from MY_TestPlat.server import db_session


class RecordDao:

    def list_by_plan_id(self, plan_id):
        # 根据id返回数据
        return db_session.query(RecordModel).filter_by(plan_id=plan_id).all()

    def list(self):
        # 返回所有数据
        return db_session.query(RecordModel).all()

    def create(self, recordmodel: RecordModel):
        # 新增数据
        db_session.add(recordmodel)
        db_session.commit()
        return recordmodel.id