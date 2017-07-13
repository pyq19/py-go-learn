// 在数组中寻找某个特定整型值的存储位置，并返回一个指向该位置的指针

#include <stdio.h>

int *
find_int( int key, int array[], int array_len )
{
    int i;

    // 对于数组中的每个位置 ...
    for( i = 0; i < array_len; i += 1 )
        // 检查这个位置的值是否为需要查找的值
        if( array[i] == key )
            return &array[i];
    return NULL;
}

// int main(void){
//     int *res;
//     res = find_int(100);
//     printf(res);
// }
