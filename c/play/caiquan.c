#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    char gamer;     // 玩家出拳
    int computer;   // 电脑出拳
    int result;     // 比赛结果
    
    while (1) {
        printf(" 输入拳头:\n");
        printf("A 剪刀\nB 拳头\nC 布\n");
        scanf("%c%*c", &gamer);
        switch (gamer) {
            case 65:    // A
            case 97:    // a
                gamer = 4;
                break;
            case 66:    // B
            case 98:    // b
                gamer = 7;
                break;
            case 67:    // C
            case 99:    // c
                gamer = 10;
                break;
            case 68:    // D
            case 100:   // d
                return 0;

            default:
                printf(" choose %c error\n", gamer);
                getchar();
                system("cls");  // 清屏幕
                return 0;
                break;
        }

        srand((unsigned)time(NULL));    // 随机数种子
        computer = rand() % 3;          // 产生随机数并取余，得到电脑出拳
        result = (int)gamer + computer; // gamer 为char 类型，数学运算时要强制转换类型
        printf("电脑出->");
        switch(computer){
            case 0: printf("剪刀\n"); break;    // 4 1
            case 1: printf("石头\n"); break;    // 7 2
            case 2: printf("布\n"); break;      // 10 3
        }
        printf("你出->");
        switch(gamer){
            case 4: printf("剪刀\n"); break;
            case 7: printf("石头\n"); break;
            case 10:printf("布\n"); break;
        }
        if (result==6 || result == 7 || result == 11) printf(" you win");
        else if (result == 5 || result == 9 || result == 10) printf(" com win");
        else printf(" pingshou");
        system("pause>nul&&cls");   // 暂停并清屏
    }
    return 0;

}
