#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
    //given an index in argv[1], return the corresponding argument from argv[]
    //-tabnine next line-
    int index = atoi(argv[1]);
    if (index >= 0 && index < argc) {
        return atoi(argv[index + 1]);
    } else {
        return -1;
    }
}


    
}