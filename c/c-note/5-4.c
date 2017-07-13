// longjmp

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <setjmp.h>

void test(jmp_buf *env)
{
    printf("1....\n");
    longjmp(*env, 10);
}

int main(int argc, char* argv[])
{
    jmp_buf env;
    int ret = setjmp(env);

    if (ret == 0)
    {
        test(&env);
    }
    else
    {
        printf("2....(%d)\n", ret);
    }

    return EXIT_SUCCESS;
}
// 1....
// 2....(10)
