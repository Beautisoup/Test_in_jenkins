import jenkinsapi  # 导入 jenkinsapi 库用于与 Jenkins 交互
import pytest  # 导入 pytest 库用于测试
from _pytest import mark  # 导入 pytest 的标记功能
from jenkinsapi.jenkins import Jenkins  # 从 jenkinsapi 中导入 Jenkins 类


class Test_Plat_jenkins():
    BASE_URL = 'http://localhost:8083/'  # Jenkins 服务器的基础 URL
    USERNAME = 'liyuanrui'  # 用于 Jenkins 登录的用户名
    PASSWORD = '112ccdbaf45890a48ea1d5250e2af6d493'  # 用于 Jenkins token
    JOB = 'allure_demo'  # 要操作的 Jenkins 作业名称

    @pytest.mark.skip(reason="skip this test")
    def test_jobs(self):
        # 创建 Jenkins 实例
        server = jenkinsapi.jenkins.Jenkins(self.BASE_URL, username=self.USERNAME, password=self.PASSWORD)
        # 获取所有 Jenkins 作业信息
        jobs = server.get_jobs()
        # 打印每个作业的名称及其 URL
        for job in jobs:
            print(job)

    def test_invoke_job(self):
        # 创建 Jenkins 实例
        server = jenkinsapi.jenkins.Jenkins(self.BASE_URL, username=self.USERNAME, password=self.PASSWORD)

        # 获取 Jenkins 中的特定作业
        job = server.get_job(self.JOB)
        if job:
            print(f"Building job {self.JOB}...")
            job.invoke()  # 触发作业构建

            # 从作业对象获取最后一次构建编号（+1 代表下一次构建）
            last_build_number = job.get_last_buildnumber() + 1
            print(f"Next build number for job {self.JOB}: {last_build_number}")  # 输出下一次构建编号

            # 构建报告的 URL
            report_url = f'{self.BASE_URL}job/{self.JOB}/{last_build_number}/allure/'
            print(report_url)  # 打印生成的报告 URL
            return report_url
        else:
            # 如果作业未找到则输出错误信息
            print(f"Job {self.JOB} not found.")

# 如果此脚本是主程序，则用 pytest 运行
if __name__ == '__main__':
    pytest.main()
