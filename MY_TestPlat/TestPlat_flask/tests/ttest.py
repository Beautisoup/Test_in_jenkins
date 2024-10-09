from passlib.handlers.sha2_crypt import sha256_crypt

class UserMo:
    def __init__(self, *args, **kwargs):
        # 密码进行自动加密
        self.username = kwargs.get('username')
        self.password = sha256_crypt.hash(kwargs.get('password'))



    def check_hash_password(self, raw_password):
        '''
        校验密码
        :param raw_password: 传入的密码
        :return: 校验结果 True or False
        '''
        return sha256_crypt.verify(raw_password, self.password),self.password

if __name__ == '__main__':
    user = UserMo(username = 'liyuan', password = '123456')
    print(user.check_hash_password('123456'))