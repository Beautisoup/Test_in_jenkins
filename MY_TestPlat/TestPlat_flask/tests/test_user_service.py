import pytest

from MY_TestPlat.TestPlat_flask.model.user_model import UserModel
from MY_TestPlat.TestPlat_flask.service.user_service import UserService
from MY_TestPlat.server import app  # 确保这里导入的是正确的 Flask 实例

@pytest.fixture
def user_service():
    # 在测试之前推送 Flask 应用上下文
    with app.app_context():
        yield UserService()

class Test_User_Service:
    def setup_method(self, method):
        self.user_service = UserService()
        user_data = [
            {
                'id': 1,
                'username': 'admin',
                'password': '<PASSWORD>',
            }
        ]
        self.user = UserModel(id=1, username="test_user1", password="nssb")
    def test_get(self):
        user = self.user_service.get(3)
        print(user.as_dict())
        assert user.username == "test_user1"

    def test_get_user(mocker):
        mock_user = UserModel(id=1, username="test_user")
        mocker.patch("MY_TestPlat.TestPlat_flask.service.user_service.user_dao.get", return_value=mock_user)

        user_service = UserService()
        result = user_service.get(1)

        assert result.id == 1
        assert result.username == "test_user"

    def test_get_by_name(self):
        assert False

    def test_create(self):
         user = UserModel(username="AA", password="123456")
         user_id = self.user_service.create(user)
         assert user_id ==4

    # def test_create_access_token(self, user_service):
    #     user = UserModel(username="test_user1", password="nssb")
    #     # 在此处推送应用上下文
    #     with app.app_context():
    #         token = user_service.create_access_token(user)
    #     print(token)
    #     assert token

    def test_create_access_token(self, user_service):
        user = UserModel(username="test_user1", password="nssb")
        # 不需要 app.app_context()，直接调用 create_access_token
        token = user_service.create_access_token(user)

        print(token)
        assert token  # 验证 token 是否正确生成
