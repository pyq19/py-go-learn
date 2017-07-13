// 指针参数和返回值

#include <stdio.h>

int *swap(int *px, int *py)
{
    int temp;
    temp = *px;
    *px = *py;
    *py = temp;
    return px;
}

int main(void)
{   
    int i = 10, j = 20;
    printf("new i = %d, j = %d", i, j);
    int *p = swap(&i, &j);
    printf("new i = %d, j = %d, *p = %d\n", i, j, *p);
    return 0;
}
