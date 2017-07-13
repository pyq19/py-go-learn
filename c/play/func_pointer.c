// 函数指针
// http://www.cnblogs.com/windlaughing/archive/2013/04/10/3012012.html

/*
#include <stdio.h>

void my_func(int x); // 声明也可以写成void my_func( int );

int main()
{
    my_func(100);   // 一般的函数调用
    return 0;
}

void my_func(int x)
{
    printf("my_func -> %d\n", x);
}
*/


// 函数指针变量
// 数据变量的内存地址可以存储在相应的指针变量中，
// 函数的首地址也可以存储在某个函数指针变量中。
// 这样可以通过这个函数指针变量来调用所指向的函数.
// void (*func_p)(int); // 声明一个指向同样参数与返回值的函数指针变量

#include <stdio.h>
#include <stdlib.h>

void (*func_p)(int);    // 也可写成void (*func_p)(int x)
void (*func_a)(int);
void my_func(int x);    // 也可写成void my_func(int)

int main(void)
{
    // 一般的函数调用
    my_func(100);

    // my_func 与 func_p 的类型关系类似于int 与int *
    func_p = &my_func;  // 将my_func 函数的地址赋给func_p 变量
    (*func_p)(200);     // 通过函数指针变量来调用函数

    // my_func 与 func_a 的类型关系类似于int 与int
    func_a = my_func;
    func_a(300);

    func_p(400);
    (*func_a)(600);
    (*my_func)(1000);

    return 0;
}

void my_func(int x)
{
    printf("my_func -> %d\n", x);
}
// my_func -> 100
// my_func -> 200
// my_func -> 300
// my_func -> 400
// my_func -> 600
// my_func -> 1000

// my_func 的函数名与func_p func_a 函数指针都是一样的，即都是·函数指针·
// my_func 函数名是一个·函数指针常量·
// func_p func_a 是·函数指针变量·
