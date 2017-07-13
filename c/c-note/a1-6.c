// 1.6 函数指针
// 默认情况下，函数名就是指向该函数的指针常量

/*
#include <stdio.h>

void inc(int* x) {
    *x += 1;
}

int main(void) {
    void (*f)(int*) = inc;

    int i = 100;
    f(&i);
    printf("%d\n", i);

    inc(&i);
    printf("%d\n", i);

    return 0;
}
// 101
*/

/* ------------ */

/*
// 定义一个函数指针类型
typedef void (*inc_t)(int*);

int main(void)
{
    inc_t f = inc;
}
*/

/* ----------- */

// 定义函数指针类型 typedef void(*inc_t)(int*)
// 定义函数类型 typedef void(inc_t)(int*)

#include <stdio.h>
#include <stdlib.h>

void test()
{
    printf("test");
}

typedef void(func_t)();
typedef void(*func_ptr_t)();

int main(int argc, char* argv[])
{
    func_t* f = test;
    func_ptr_t p = test;

    f();
    p();

    return EXIT_SUCCESS;
}
// testtest%
