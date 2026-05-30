from dask.array import delete
from dask.config import update


def adminMenu(userList):
    """
    管理员菜单
    :param userList:
    :return:
    """
    menu1 = '''
                        ********管理员界面*********
                        1.查看用户信息
                        2.修改用户信息
                        3.删除用户信息
                        4.退出
                        请选择：
                        '''
    while True:
        c=input(menu1)
        if c=='1':
            selectUser(userList)
        elif c=='2':
            updateUser(userList)
        elif c=='3':
            delUser(userList)
        else:
            exit()

def selectUser(userList):
    """
    查看用户信息
    :param userList:
    :return:
    """
    print('查询用户信息,')
    input(userList)
    for user in userList:
        print(user)
def updateUser(userList):
    """
    修改用户信息
    :param userList:
    :return:
    """
    print('修改用户信息')
    input()
def delUser(userList):
    """
    删除用户信息
    :param userList:
    :return:
    """
    print('删除用户信息')
    input()
