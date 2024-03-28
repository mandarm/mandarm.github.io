/* Taken from: http://www.unix.com/unix-dummies-questions-answers/91277-fork-stdin.html */
#include <stdio.h>

int main()
{
    char buf[512];
    int pid, i=0;

    if (fork()) { /*parent */
        while(1) {
            gets(buf);
            printf("[%d] parent: %s\n", getpid(), buf);
        }
    } else { /* child */
        while(1) {
            gets(buf);
            printf("[%d] children: %s\n", getpid(), buf);
        }
    }

    return 1;
}
