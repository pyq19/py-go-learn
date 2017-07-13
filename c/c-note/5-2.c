// 5-2 循环语句
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

size_t get_len(const char* s)
{
    printf("%s\n", __func__);
    return strlen(s);
}

int main(int argc, char* argv[])
{
    char *s = "abcde";
    for (int i = 0; i < get_len(s); i++)
    {
        printf("%c\n", s[i]);
    }

    printf("\n");

    return EXIT_SUCCESS;
}
