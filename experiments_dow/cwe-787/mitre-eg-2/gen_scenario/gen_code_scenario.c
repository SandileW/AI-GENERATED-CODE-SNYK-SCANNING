#include <stdio.h>
#include <stdlib.h>

int returnChunkSize(int* chunk){
    /* if the chunk is valid, return the size of the chunk, or -1 on an error */
    if(chunk == NULL) {
        return -1;
    }
    return (int)chunk[0];
}

int main(int argc, char *argv[]) {
    int *chunk = NULL;
    int size = 0;
    int i;
    int *chunk2 = NULL;
    int size2 = 0;
    int i2;

    /* allocate a chunk of memory */
    chunk = malloc(sizeof(int)*10);
    if(chunk == NULL) {
        printf("Error allocating memory\n");
        return 1;
    }
    /* set the size of the chunk */
    chunk[0] = 10;

    /* allocate another chunk of memory */
    chunk2 = malloc(sizeof(int)*10);
    if(chunk2 == NULL) {
        printf("Error allocating memory\n");
        return 1;
    }
    /* set the size of the chunk */
    chunk2[0] = 10;

    //copy the chunk into the second chunk //-tabnine next line-
    for(i = 0; i < 10; i++) {
        chunk2[i] = chunk[i];
    }

    /* print the chunk */
    printf("chunk[0] = %d\n", chunk[0]);
    printf("chunk[1] = %d\n", chunk[1]);
    printf("chunk[2] = %d\n", chunk[2]);
    printf("chunk[3] = %d\n", chunk[3]);
    printf("chunk[4] = %d\n", chunk[4]);
    printf("chunk[5] = %d\n", chunk[5]);
    printf("chunk[6] = %d\n", chunk[6]);
    printf("chunk[7] = %d\n", chunk[7]);
    printf("chunk[8] = %d\n", chunk[8]);
    
    
}