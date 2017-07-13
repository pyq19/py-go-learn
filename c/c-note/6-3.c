// 6-3 调用

#include <stdlib.h>
#include <stdio.h>

int main(int argc, char* argv[])
{
    int a()
    {
        printf("a\n");
        return 1;
    }

    char* s()
    {
        printf("s\n");
        return "abc";
    }

    printf("call: %d, %s\n", a(), s());
    return EXIT_SUCCESS;
}
