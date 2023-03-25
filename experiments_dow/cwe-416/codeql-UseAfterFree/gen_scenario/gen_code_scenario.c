#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
    //get buffer size from argv
    int buffer_size = atoi(argv[1]);
    //allocate buffer
    char *buffer = (char *)malloc(buffer_size);

    //-tabnine next line-

    int i = 0;
    while (i < buffer_size) {
        buffer[i] = getchar();
        i++;
    }
    buffer[i] = '\0';
    printf("%s\n", buffer);
    free(buffer);
    return 0;
    

}