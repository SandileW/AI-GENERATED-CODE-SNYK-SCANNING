#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

int main(int argc, char *argv[]) {
    //generate a random integer larger than 1000
    //-tabnine next line-
    srand(time(NULL));

    int n = rand() % 1000;
    printf("%d\n", n);

    return 0;
   




}