import pytest


def test_addition():
    assert 1 + 1 == 2
if __name__ == '__main__':
    pytest.main(['--alluredir=allure-results'])