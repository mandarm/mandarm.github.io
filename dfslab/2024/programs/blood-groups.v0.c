#include <stdio.h>

int main(void)
{
    /* declarations */
    int c;
    unsigned int a, b, ab, o;
    unsigned int n, i;

    a = 0; b = 0; ab = 0; o = 0;
    printf("Enter the number of students: ");
    scanf("%d", &n); getchar(); 
    for (i = 1; i <= n; i++) {
        printf("Enter the blood group of mtc15%02d: ", i);
        c = getchar(); getchar();
        if (c == 'A')
            a = a + 1;
        else if (c == 'B')
            b = b + 1;
        else if (c == 'a')
            ab = ab + 1;
        else if (c == 'O')
            o = o + 1;
        else
            printf("Invalid blood group %c, skipping\n", c);
    }
    printf("Number of students with blood group A: %d\n", a);
    printf("Number of students with blood group B: %d\n", b);
    printf("Number of students with blood group AB: %d\n", ab);
    printf("Number of students with blood group O: %d\n", o);

    return 0;
}
