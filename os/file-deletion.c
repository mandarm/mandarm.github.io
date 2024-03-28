#include "common.h"
#include <sys/types.h>
#include <sys/stat.h>
#include <unistd.h>

int main(int ac, char *av[])
{
    char filename[BUF_LEN];
    int fd;
    struct stat statinfo;

    strcpy(filename, "tmpfileXXXXXX");
    if (-1 == (fd = mkstemp(filename)))
        ERR_MESG("file-deletion: error creating / opening tmp file");
    fprintf(stderr, "Please delete the file %s now.\n", filename);
    sleep(10);
    if (BUF_LEN != write(fd, filename, BUF_LEN))
        perror("file-deletion: error in writing");
    if (-1 == stat(filename, &statinfo))
        perror("file-deletion: error in stat");    
    if (-1 == fstat(fd, &statinfo))
        ERR_MESG("file-deletion: error in fstat");
    fprintf(stderr, "Inode no: %d, size: %d\n", (int) statinfo.st_ino,
            (int) statinfo.st_size);
    close(fd);
    return 0;
}
