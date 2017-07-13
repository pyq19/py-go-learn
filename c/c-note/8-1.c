// void* 又被称为万能指针，可以代表任何对象的地址，但没有该对象的类型，即必须转型后才能进行对象操作
// void* 指针可以与其它任何类型指针进行隐式转换

#include <stdio.h>
#include <stdlib.h>

void test(void* p, size_t len)
{
    unsigned char* cp = p;

    for (int i = 0; i < len; i++)
    {
        printf("%02x ", *(cp + i));
    }
    printf("\n");
}

int main(int argc, char* argv[])
{
    int x = 0x00112233;
    test(&x, sizeof(x));

    return EXIT_SUCCESS;
}
// 33 22 11 00
