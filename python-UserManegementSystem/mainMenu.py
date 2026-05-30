from login import login
import Register
import adminMenu
import userMenu
#开始界面
user1={'name':'lili','password':'123456','role':'普通用户'}
user2={'name':'admin','password':'123456','role':'管理员'}
#列表里面套字典，一个字典是一个用户
user=[
    {'name':'lili','password':'123456','role':'普通用户'},
    {'name':'admin','password':'123456','role':'管理员'}
]

menu='''
************欢迎使用用户管理系统*****************
1.登录
2.注册
3.退出
请选择：
'''

flag=True
#nowUser
while flag:
    choose=int(input(menu))
    if choose==1:
        r=login(user)
        if  r!= None:#登录成功的情况
            nowUser=r
            if nowUser['role']=='管理员':
                r1=adminMenu.adminMenu(user)
                if r1!=4:
                    flag=False
            elif nowUser['role']=='普通用户':
                r2=userMenu.userMenu(user)

    elif choose==2:
        r=Register.register(user)
    else:
        exit()