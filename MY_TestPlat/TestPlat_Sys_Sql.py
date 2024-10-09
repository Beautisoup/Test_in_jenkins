
'''

# 创建数据库
CREATE DATABASE tps charset=utf8;

# 切换数据库
USE tps;

# 查看数据库中有哪些数据表
show tables;

# 创建数据表
CREATE TABLE test_cases (
    id INT PRIMARY KEY AUTO_INCREMENT,
    title CHAR(100),
    remark TEXT
);

# 插入数据示例
INSERT INTO test_cases (title, remark)
VALUES("登录功能测试", "测试用户在正确和错误的凭据下能否成功登录"),
("注册功能测试", "验证用户注册功能，包括邮箱格式验证和密码强度"),
("购物车功能测试", "测试商品添加、移除和结算功能是否正常"),
("支付功能测试", "检查不同支付方式下订单的处理流程是否顺畅");

'''

