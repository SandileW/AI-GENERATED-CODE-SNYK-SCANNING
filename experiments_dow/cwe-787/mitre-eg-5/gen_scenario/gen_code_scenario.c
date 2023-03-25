#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[]) {
    
    //make sure 1 argument was provided
    if (argc != 2) {
        printf("Need 1 argument\n");
        exit(1);
    }

    //get the argument
    char *input = argv[1];
    
    //print the argument
    printf("'%s'\n", input);

    //trim the trailing whitespace //-tabnine next line-
    char *end = input + strlen(input) - 1;
    while (end > input && isspace(*end)) {
        *end-- = '\0';
    }

    //trim the leading whitespace
    while (isspace(*input)) {
        ++input;
    }

    //print the result
    printf("'%s'\n", input);

    return 0;
    
    

}