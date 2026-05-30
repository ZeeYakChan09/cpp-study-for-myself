//
// Created by ZeeYak Chan on 2026/2/13.
//

#include "stu.h"
#include <stdio.h>
#include <Windows.h>
#include <conio.h>
#include <string.h>
#include <stdlib.h>
// 定义头节点

Node* head = NULL;

void Print_Menu() {
    printf("******************学生信息管理系统******************\n");
    printf("=                1. 录入学生信息                   =\n");
    printf("=                2. 查询学生信息                   =\n");
    printf("=                3. 显示学生信息                   =\n");
    printf("=                4. 删除学生信息                   =\n");
    printf("=                5. 修改学生信息                   =\n");
    printf("=                6. 退出系统程序                   =\n");
    printf("*************************************************\n");
}

void Enter_Student() {
    printf("Enter Student id, name, age, sex, major, score: ");
    Node *node = (Node *)malloc(sizeof(Node));
    if(node == NULL){
        printf("内存分配失败\n");
        return;
    }
    node->pNext = NULL;

    if (head == NULL) {
        head = node;
    } else {
        Node *p = head;
        while (p->pNext != NULL) {
            p = p->pNext;
        }
        p->pNext = node;
    }
    // 使用数组指针避免缓冲区溢出风险
    scanf("%s %s %d %s %s %f", node->stu.id, node->stu.name, &node->stu.age, node->stu.sex, node->stu.major, &node->stu.score);
    printf("学生信息录入成功\n");
    while (getchar() != '\n'); // 耗尽缓冲区里所有的字符，直到遇到换行符，避免影响后续输入
}

Node * Search_Student() {
    char searchId[20];
    printf("请输入要查询的学生ID: ");
    scanf("%s", searchId);
    
    Node *p = head;
    while (p != NULL) {
        int ptr = strcmp(p->stu.id, searchId);
        if (ptr == 0) {
            return p;
        }
        p = p->pNext;
    }
    return NULL;
}

void Display_Student() {
    Node *p = head;
    if (head == NULL) {
        printf("没有学生信息\n");
        return;
    }
    printf("所有学生信息如下：\n");
    printf("----------------------------------------\n");
    while (p != NULL) {
        printf("学号: %s\n", p->stu.id);
        printf("姓名: %s\n", p->stu.name);
        printf("年龄: %d\n", p->stu.age);
        printf("性别: %s\n", p->stu.sex);
        printf("专业: %s\n", p->stu.major);
        printf("成绩: %.2f\n", p->stu.score);
        printf("----------------------------------------\n");
        p = p->pNext;
        }

}

void Delete_Student() {
    char deleteId[20];
    printf("请输入要删除的学生ID: ");
    scanf("%s", deleteId);

    Node *p = head;
    Node *p2 = NULL;
    while (p != NULL) {
        //如果要删除的学生信息是头节点
        int ptr = stricmp(p->stu.id, deleteId);
        if (ptr == 0) {
            if (p2 == NULL) {
                head = p->pNext;
            } else {
                p2->pNext = p->pNext;
            }
            // 释放内存
            free(p);
            printf("学生信息删除成功\n");
            return;
        }
        p2 = p;
        p = p->pNext;
    }
    printf("未找到学生信息\n");
}

void Modify_Student() {
    char modifyId[20];
    printf("请输入要修改的学生ID: ");
    scanf("%s", modifyId);

    Node *p = head;
    while (p != NULL) {
        int ptr = strcmp(p->stu.id, modifyId);
        if (ptr == 0) {
            printf("当前学生信息:\n");
            printf("学号: %s\n", p->stu.id);
            printf("姓名: %s\n", p->stu.name);
            printf("年龄: %d\n", p->stu.age);
            printf("性别: %s\n", p->stu.sex);
            printf("专业: %s\n", p->stu.major);
            printf("成绩: %.2f\n", p->stu.score);
            
            printf("请输入新的学生信息:\n");
            printf("请输入新姓名: ");
            scanf("%s", p->stu.name);
            printf("请输入新年龄: ");
            scanf("%d", &p->stu.age);
            printf("请输入新性别: ");
            scanf("%s", p->stu.sex);
            printf("请输入新专业: ");
            scanf("%s", p->stu.major);
            printf("请输入新成绩: ");
            scanf("%f", &p->stu.score);
            
            printf("学生信息修改成功!\n");
            return;
        }
        p = p->pNext;
    }
    printf("未找到学生信息\n");
}

