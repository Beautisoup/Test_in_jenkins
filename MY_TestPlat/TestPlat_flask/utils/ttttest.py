import subprocess
import pytest

class Test_Plat_jenkins():
    @pytest.mark.run(order=4)
    @pytest.mark.skip(reason="skip this test")
    def test_jobs(self):
        print('test_jobs')

    @pytest.mark.run(order=1)
    def test_invoke_job(self):
        print("Running test_invoke_job")
        # 测试逻辑

    @pytest.mark.run(order=3)
    def test_invoke_job2(self):
        print("Running test_invoke_job2")
        # 测试逻辑

    @pytest.mark.run(order=2)
    def test_invoke_job3(self):
        print("Running test_invoke_job3")
        # 测试逻辑

if __name__ == '__main__':
    pytest.main(['-k', 'test_invoke_job2','-v'])

    '''
    安装依赖包
    pip install pytest-ordering
    '''
