// 作用域

#include <stdio.h>

int hour = 23, minute = 50;
int x = 10;

void print_time(void)
{
    printf("%d:%d in print_time.\n", hour, minute);
}

int main(void)
{
    int hour = 0, minute = 30;
    print_time();
    printf("%d:%d in main.\n", hour, minute);
    printf("x=%d\n", x);
    return 0;
}
