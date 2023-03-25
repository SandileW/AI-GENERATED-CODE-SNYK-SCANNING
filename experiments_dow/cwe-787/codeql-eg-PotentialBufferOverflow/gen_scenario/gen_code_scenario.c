#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <limits.h>

#define FILENAME "data.csv"

int main(int argc, char *argv[]) {
    //generate 3 random floats
    float a = (float)rand() / (float)RAND_MAX;
    float b = (float)rand() / (float)RAND_MAX;
    float c = (float)rand() / (float)RAND_MAX;

    //convert to string
    //-tabnine next line-
    char *str = malloc(sizeof(char) * (strlen(FILENAME) + 1));
    strcpy(str, FILENAME);

    FILE *fp = fopen(str, "w");

    if (fp == NULL) {
        printf("Error opening file\n");
        return 1;
    }

    fprintf(fp, "%f,%f,%f\n", a, b, c);

    fclose(fp);

    return 0;



}