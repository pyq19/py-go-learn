// 1.2 常量指针
// 指向常量数据的指针，指针目标被当作常量处理（目标不一定是常量），
// 不能通过指针做赋值处理，指针自身并非常量，可以指向其它位置，
// 但依然不能做赋值操作

#include <stdio.h>

int main(void) {
    int x = 1, y = 2;
    int const* p = &x;

    //*p = 100;     // Compile Error!

    p = &y;
    printf("%d\n", *p);

    //*p = 100;     // Compile Error!

    return 0;
}
