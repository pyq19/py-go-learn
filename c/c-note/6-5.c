// 可选性自变量

#include <stdarg.h>
#include <stdlib.h>
#include <stdio.h>

/* 指定自变量数量 */
void test(int count, ...)
{
    va_list args;
    va_start(args, count);

    for (int i = 0; i < count; i++)
    {
        int value = va_arg(args, int);
        printf("%d\n", value);
    }

    va_end(args);
}

/* 以 NULL 为结束标记 */
void test2(const char* s, ...)
{
    printf("%s\n", s);

    va_list args;
    va_start(args, s);

    char* value;
    do
    {
        value = va_arg(args, char*);
        if (value) printf("%s\n", value);
    }
    while (value != NULL);

    va_end(args);
}

/* 直接将 va_list 传递给其它可选自变量函数 */
void test3(const char* format, ...)
{
    va_list args;
    va_start(args, format);

    vprintf(format, args);

    va_end(args);
}

int main(int argc, char* argv[])
{
    test(3, 11, 22, 33);
    test2("hello", "aa", "bb", "cc", "dd", NULL);
    test3("%s, %d\n", "hello, world!", 12345);

    return EXIT_SUCCESS;
}
