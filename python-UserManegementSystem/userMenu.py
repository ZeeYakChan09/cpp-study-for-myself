import SearchMenu
import adminMenu
from UserManegementSystem.adminMenu import updateUser


def userMenu(userList):
    menu2 = '''
            ********用户界面**********
            1.查看用户信息
            2.修改用户信息
            3.退出
            请选择：
            '''
    while True:
        c=input(menu2)
        if c=='1':
            adminMenu.selectUser(userList)
        elif c=='2':
            adminMenu.updateUser(userList)
        elif c=='3':
            break
