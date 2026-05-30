def register(userList):
    """
    用户注册
    :param userList:
    :return: True-注册成功 False-注册失败
    """
    # 注册
    name = input('请输入用户名：')

    for user in userList:
        if name == user['name']:
            print('用户已存在')
            return None
    else:
        pwd = input('请输入密码：')
        repwd = input('请再次输入密码：')
        if pwd != repwd:
            print('两次输入不正确')
            return None
        else:
            role = input('请输入角色：')
            if role == '普通用户':
                newUser = {'name': name, 'password': pwd, 'role': '普通用户'}
            elif role == '管理员':
                newUser = {'name': name, 'password': pwd, 'role': '管理员'}
            else:
                print('角色输入错误')
                return None

            print('注册成功')
            userList.append(newUser)
            print(userList)
            return True
