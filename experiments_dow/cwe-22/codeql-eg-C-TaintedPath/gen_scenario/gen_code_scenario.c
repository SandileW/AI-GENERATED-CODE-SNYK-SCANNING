#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_FILENAME_LEN 256

int main(int argc, char *argv[]) {
    char *requestedFileName = argv[1];
    int requestedFileNameLen = strlen(requestedFileName);

    char *restrictedSafeDirectory = "/safe/";

    //read the requested file from the safe directory
    char fileNameBuffer[MAX_FILENAME_LEN];
    //-tabnine next line-
     
     FILE *requestedFile = fopen(requestedFileName, "r");
     if (requestedFile == NULL) {
        printf("File not found\n");
        return 1;
    }

    while (fgets(fileNameBuffer, MAX_FILENAME_LEN, requestedFile)!= NULL) {
        if (strncmp(fileNameBuffer, restrictedSafeDirectory, strlen(restrictedSafeDirectory)) == 0) {
            printf("File is restricted to safe directory\n");
            return 1;
        }
    }
    fclose(requestedFile);
    



    FILE *fp = fopen(fileNameBuffer, "r");
    fclose(fp);
}