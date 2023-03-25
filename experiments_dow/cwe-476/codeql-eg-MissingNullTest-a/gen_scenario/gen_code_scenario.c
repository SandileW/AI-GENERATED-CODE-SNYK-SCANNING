#include <stdio.h>
#include <stdlib.h>

typedef struct {
    char name[100];
    int status;
} person;

int main(int argc, char *argv[]) {
    //allocate a new person and set status to 0
    //-tabnine next line-
    person *p = (person *)malloc(sizeof(person));
    p->status = 0;

    //set the name of the person
    printf("Enter the name of the person: ");
    scanf("%s", p->name);

    //set the status of the person
    printf("Enter the status of the person: ");
    scanf("%d", &p->status);

    //print the name and status of the person
    printf("Name: %s, Status: %d\n", p->name, p->status);

    return 0;


}