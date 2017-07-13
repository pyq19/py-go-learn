// 9-4 定义
// 定义结构类型

#include <stdio.h>
#include <stdlib.h>

int main(int argc, char* argv[])
{
    /* 直接定义结构类型和变量 */
    struct { int x; short y; } a = { 1, 2 }, a2 = {};
    printf("a.x = %d, a.y = %d\n", a.x, a.y);
    // a.x = 1, a.y = 2

    /* 函数内部也可定义结构类型 */
    struct data { int x; short y; };

    struct data b = { .y = 3 };
    printf("b.x = %d, b.y = %d\n", b.x, b.y);
    // b.x = 0, b.y = 3

    /* 复合字面值 */
    struct data* c = &(struct data){ 1, 2 };
    printf("c.x = %d, c.y = %d\n", c->x, c->y);
    // c.x = 1, c.y = 2

    /* 也可以直接将结构体类型定义放在复合字面值中 */
    void* p = &(struct data2 { int x; short y; }){ 11, 22 };

    /* 相同内存布局的结构体可以直接转换 */
    struct data* d = (struct data*)p;
    printf("d.x = %d, d.y = %d\n", d->x, d->y);
    // d.x = 11, d.y = 22

    return EXIT_SUCCESS;
}
