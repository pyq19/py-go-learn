// 验证局部变量存储空间的分配和释放

#include <stdio.h>

void foo(void)
{
    int i;
    printf("%d\n", i);
    i = 7777;
}

int main(void)
{
    foo();
    foo();
    return 0;
}

// out:
// 0
// 7777
