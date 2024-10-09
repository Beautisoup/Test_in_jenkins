# 调用 jenkins
# utils/jenkins_util.py

from jenkinsapi.jenkins import Jenkins

#在自己本地搭建Jenkins服务    视频2：12：30处

class JenkinsUtils:
    # Jenkins 服务
    BASE_URL = "http://localhost:8083/"
    # Jenkins 服务对应的用户名
    USERNAME = "liyuanrui"
    # Jenkins 服务对应的token
    PASSWORD = "112ccdbaf45890a48ea1d5250e2af6d493"
    # Jenkins 要操作的 Job 名称
    JOB = "test_plat_job"

    @classmethod
    def invoke(cls, invoke_params):
        """
        执行构建任务
        :return:
        """
        # 获取 Jenkins 对象
        jenkins_hogwarts = Jenkins(cls.BASE_URL, cls.USERNAME, cls.PASSWORD)
        # 获取 Jenkins 的 job 对象
        job = jenkins_hogwarts.get_job(cls.JOB)
        # 构建 hogwarts job，传入的值必须是字典，key 对应 jenkins 设置的参数名
        # job.invoke(build_params={
        #     "step": "xx.py::TestXX::test_xx",
        #     "methods": "pytest"
        # })
        job.invoke(build_params=invoke_params)
        # 获取job 最后一次完成构建的编号
        last_build_number = job.get_last_buildnumber() + 1
        # 执行方式为：pytest 用例名称 指定报告生成地址
        # 生成报告格式为
        # http://127.0.0.1:5003/job/test_platform_job/22/allure/
        # 获取本次构建的报告地址
        report = f"{cls.BASE_URL}job/{cls.JOB}/{last_build_number}/allure/"
        return report