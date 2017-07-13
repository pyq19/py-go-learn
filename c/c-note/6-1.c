// 函数 嵌套

#include <stdlib.h>
#include <stdio.h>

typedef void(*func_t)();

func_t test()
{
    void func1()
    {
        printf("%s\n", __func__);
    };

    return func1;
}

int main(int argc, char* argv[])
{
    test()();
    return EXIT_SUCCESS;
}
