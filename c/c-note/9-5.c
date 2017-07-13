// 9-5 初始化
// 结构体的初始化和数组一样简洁，包括使用初始化器初始化特定的某些成员，
// 未被初始化器初始化的成员将被设置为0

#include <stdio.h>
#include <stdlib.h>

typedef struct
{
    int x;
    short y[3];
    long long z;
} data_t;

int main(int argc, char* argv[])
{
    data_t d = {};
    data_t d1 = { 1, { 11, 22, 33 }, 2LL };
    data_t d2 = { .z = 3LL, .y[2] = 2 };

//    printf("x: %s, y: %s", d.x, d.y);
//    printf("x: %s, y: %s", d1.x, d1.y);
//    printf("x: %s, y: %s", d2.x, d2.y);

    return EXIT_SUCCESS;
}
