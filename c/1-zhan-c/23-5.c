// 23.5 返回指向已分配内存的指针

#include <string.h>
#include "23-5.h"

static const char *msg[] = {
    "Sunday", "Monday", "Tuesday", "Thursday", "Friday", "Saturday"
};

char *get_a_day(int idx)
{
    static char buf[20];
    strcpy(buf, msg[idx]);
    return buf;
}
