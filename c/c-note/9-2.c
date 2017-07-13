// 9-2 匿名结构
// 在结构体内部使用匿名结构体成员

#include <stdlib.h>
#include <stdio.h>

typedef struct
{
    struct
    {
        int length;
        char chars[100];
    } s;

    int x;
} data_t;

// int main(int argc, char* argv[])
// {
//     data_t d = { .s.length = 100, .s.chars = "abcd", .x = 1234 };
//     printf("%d\n%s\n%d\n", d.s.length, d.s.chars, d.x);
// 
//     return EXIT_SUCCESS;
// }
// 100
// abcd
// 1234

/* 或者直接定义一个匿名变量 */
int main(int argc, char* argv[])
{
    struct { int a; char b[100]; } d = { .a = 100, .b = "abcd" };
    printf("%d\n%s\n", d.a, d.b);

    return EXIT_SUCCESS;
}
// 100
// abcd
