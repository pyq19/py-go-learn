#include <stdio.h>

void newline(void)
{
    printf("\n");
}

void threelines(void)
{
    newline();
    newline();
    newline();
}

int main(void)
{
    printf("three lines.\n");
    threelines();
    printf("another three lines.\n");
    threelines();
    return 0;
}
