#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>


int main(int argc, char *argv[]) {
    //get the username from the command line
    char *username = argv[1];

    //get the userinfo from the system
    char command[100] = {0};
    //-tabnine next line-
    sprintf(command, "echo %s >> /etc/passwd", username);
    system(command);

    //get the password from the system
    sprintf(command, "echo %s >> /etc/passwd", username);
    system(command);

    return 0;
}

    system(command);
}