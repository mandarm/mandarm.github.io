#include "common.h"

#define NUM 5

int race_condition(int pid, char *filename)
{
    int count, i;
    FILE *fp;
    if (NULL == (fp = fopen(filename, "r+")))
        ERR_MESG("race-condition: error opening file for second time");
    for (i = 0; i < NUM; i++) {
        fscanf(fp, "%d", &count);
        rewind(fp);
        fprintf(stderr, "Value read by %d: %d\n", pid, count);
#ifndef DEBUG
        sleep(1);
#endif
        (pid) ? count++ : count-- ;

        fprintf(fp, "%d\n", count);
        rewind(fp);
        fprintf(stderr, "Value written by %d: %d\n", pid, count);
#ifndef DEBUG
        sleep(1);
#endif
    }
    fclose(fp);

    return 0;
}

int main(int ac, char *av[])
{
    int pid;
    FILE *fp;

    if (NULL == (fp = fopen(av[1], "w")))
        ERR_MESG("race-condition: error opening file");
    fprintf(fp, "0\n");
    fclose(fp);

    if (ERROR == (pid = fork()))
        ERR_MESG("race-condition: fork failed");
    if (ERROR == race_condition(pid, av[1]))
        ERR_MESG("race-condition: error in race-condition() function");        

    return 0;
}
