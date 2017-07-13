// 定义和访问结构体

#include <stdio.h>

int main(void)
{
    struct complex_struct { double x, y; } z;
    double x = 3.0;
    z.x = x;
    z.y = 4.0;
    if (z.y < 0)
        printf("z=%f%fi\n", z.x, z.y);
    else
        printf("z=%f+%fi\n", z.x, z.y);
    return 0;
}
