// 6-2 类型
#include <stdio.h>
#include <stdlib.h>


typedef void(func_t)();     // 函数类型
typedef void(*func_ptr_t)();// 函数指针类型

void test()
{
    printf("%s\n", __func__);
}

int main(int argc, char* argv[])
{
    func_t* func = test;    // 声明一个指针
    func_ptr_t func2 = test;// 已经是指针类型

    void (*func3)();        // 声明一个包含函数原型的函数指针变量
    func3 = test;

    func();
    func2();
    func3();

    return EXIT_SUCCESS;
}
