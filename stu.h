#ifndef STU_H
#define STU_H

#include <stdio.h>

// 定义学生结构体
typedef struct {
    char id[50];
    char name[50];
    int age;
    char sex[10];
    char major[50];
    float score;
}Student;

// 定义链表节点结构体
typedef struct tagNode {
    Student stu;// 存储学生信息
    struct tagNode *pNext;// 指向下一个节点的指针
}Node;

void Print_Menu(); // 声明
void Enter_Student(); // 声明录入学生信息函数
Node* Search_Student(); // 声明查询学生信息函数
void Display_Student();
void Delete_Student();
void Modify_Student();
#endif