def login(userList):
    """
    用户登录
    :param userList:
    :return: 登录成功返回用户，失败返回none
    """
    name = input('请输入用户名：')
    pwd = input('请输入密码：')
    for user in userList:
        if user['name'] == name and user['password'] == pwd:
            print('登录成功')
            return user
    else:
        print('登陆失败，请重新登录！')
        return None