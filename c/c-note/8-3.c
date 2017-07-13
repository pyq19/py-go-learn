// 8-3 指针运算

#include <stdio.h>
#include <stdlib.h>

int main(int argc, char* argv[])
{
    /* （1）对指针进行相等或不等运算来判断是否指向同一对象 */
    int x = 1;

    int *a, *b;
    a = &x;
    b = &x;

    printf("%d\n", a == b);
    // 1

    /* （2）对指针进行加法运算获取数组第n个元素指针 */
    int y[] = { 1, 2, 3};
    int* p = y;

    printf("%d, %d\n", y[1], *(p + 1));
    // 2, 2

    /* （3）对指针进行减法运算获取指针所在元素的数组索引序号 */
    int k[] = { 1, 2, 3};

    int* l = k;
    l++; l++;

    int index = l - k;

    printf("x[%d] = %d\n", index, k[index]);
    // x[2] = 3

    /* （4）对指针进行大小比较运算，相当于判断数组索引序号大小 */
    int o[] = { 1, 2, 3};
    int* u1 = o;
    int* u2 = o;
    u1++; u2++; u2++;

    printf("u1 < u2? %s\n", u1 < u2 ? "Y" : "N");
    // u1 < u2? Y

    /* （5）直接用&x[i] 获取指定序号元素的指针 */
    int m[] = { 1, 2, 3};

    int* n = &m[1];
    *n += 10;

    printf("%d\n", n[1]);
    // 3

    return EXIT_SUCCESS;
}
