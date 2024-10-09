import pytest

from MY_TestPlat.TestPlat_flask.service.record_service import RecordService


record = RecordService()

class Test_Record_Service_Test:
    # def setUp(self):
    #     self.record = RecordService()

    def test_list_by_plan(self):
        assert False

    def test_list(self):
        assert False

    def test_create(self):
        record_id = record.create(1)
        print(record_id)
        assert record_id

