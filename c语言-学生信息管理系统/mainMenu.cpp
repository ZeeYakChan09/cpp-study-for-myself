//
// Created by ZeeYak Chan on 2026/2/13.
//
#include <stdio.h>
#include <string.h>
#include <Windows.h>
#include "stu.h" // 现在 mainMenu.cpp 认识 Print_Menu 了
#include <conio.h>
#include <stdlib.h>

int main() {
    SetConsoleOutputCP(65001);//必须添加，否则中文会显示乱码

    while (1) {
        //system("CLS");// 这个清屏命令会清屏，但会中断程序，所以注释掉，其实就是来捣乱的，会导致打印不全
        Print_Menu();
        char ch;
        scanf(" %c", &ch);
        switch (ch) {
            case '1':
                Enter_Student();
                fflush(stdout); // 刷新输出缓冲区
                break;
            case '2': {
                Node *p = Search_Student();
                if (p != NULL) {
                    printf("找到学生信息:\n");
                    printf("学号: %s\n", p->stu.id);
                    printf("姓名: %s\n", p->stu.name);
                    printf("年龄: %d\n", p->stu.age);
                    printf("性别: %s\n", p->stu.sex);
                    printf("专业: %s\n", p->stu.major);
                    printf("成绩: %.2f\n", p->stu.score);
                }else {
                    printf("未找到学生信息\n");
                }
                fflush(stdout); // 刷新输出缓冲区
                break;
            }
            case '3':
                Display_Student();
                fflush(stdout); // 刷新输出缓冲区
                break;
            case '4':
                Delete_Student();
                fflush(stdout); // 刷新输出缓冲区
                break;
            case '5':
                Modify_Student();
                fflush(stdout); // 刷新输出缓冲区
                break;
            case '6':
                printf("退出系统,欢迎再次使用\n");
                fflush(stdout); // 刷新输出缓冲区
                return 0; // 添加退出程序的返回语句
                break;
            default:
                printf("输入错误，请重新输入\n");
                fflush(stdout); // 刷新输出缓冲区
                break;
        }
        //system("PAUSE"); // 添加暂停命令，等待用户按任意键后继续运行
        printf("\n");
    }
    return 0;
}
