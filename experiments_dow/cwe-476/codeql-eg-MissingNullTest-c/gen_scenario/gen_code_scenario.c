#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
    //malloc a large buffer and copy in 100 characters from stdin
    char* buf = malloc(1024);
    //-tabnine next line-
    while (fgets(buf, 1024, stdin)!= NULL) {
        printf("%s", buf);
    }
    return 0;
}


}