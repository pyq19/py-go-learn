// 4. 函数调用

#include <stdio.h>

int test(int x, char* s)
{
    s = "Ubuntu";
    return ++x;
}

int main(int args, char* argv[])
{
    char* s = "hello world";
    int x = 0x1234;

    int c = test(x, s);
    printf(s);

    return 0;
}
// hello world%
