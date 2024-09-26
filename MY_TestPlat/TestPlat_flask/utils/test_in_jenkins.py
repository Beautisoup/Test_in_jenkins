import pytest
import allure_pytest


def test_addition():
    assert 1 + 1 == 2, "Addition test failed"
if __name__ == '__main__':
    pytest.main(['--alluredir=allure-results'])