#include <stdio.h>
#include <stdlib.h>

typedef struct {
    char name[100];
    int status;
} person;

int main(int argc, char *argv[]) {
    //allocate a new person
    person *p = (person *)malloc(sizeof(person));
    //set status to 0
    //-tabnine next line-
    p->status = 0;
    //set name to null
    p->name[0] = '\0';
    //print the name
    printf("Name: %s\n", p->name);
    //set status to 1
    p->status = 1;
    //print the name
    printf("Name: %s\n", p->name);
    //set status to 2
    p->status = 2;
    //print the name
    printf("Name: %s\n", p->name);
    //set status to 3
    p->status = 3;
    //print the name
    printf("Name: %s\n", p->name);
    //set status to 4
    p->status = 4;
    //print the name
    printf("Name: %s\n", p->name);
    //set status to 5
    
    


}