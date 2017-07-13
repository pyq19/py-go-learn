// 6.1 字符串长度

#include <stdlib.h>
#include <stdio.h>

size_t strlen( char *string )
{
    int length = 0;

    // 依次访问字符串的内容，计数字符数，直到遇见NUL 终止符
    while( *string++ != '\0' )
        length += 1;

    return length;
}

int main(void)
{
    int s = strlen("asd");
    printf("%d", s); // 3
    return 0;
}
