// 8-4 限定符

#include <stdio.h>
#include <stdlib.h>

int main(int argc, char* argv[]){
    int x[] = {1, 2, 3};

    // 指针常量：指针本身为常量，不可修改, 但可修改目标对象
    int* const p1 = x;
    *(p1 + 1) = 22;
    printf("%d\n", x[1]); // 22

    // 常量指针：目标对象为常量，不可修改，但可修改指针
    int const *p2 = x;
    p2++;
    printf("%d\n", *p2); // 22

    return EXIT_SUCCESS;
}
