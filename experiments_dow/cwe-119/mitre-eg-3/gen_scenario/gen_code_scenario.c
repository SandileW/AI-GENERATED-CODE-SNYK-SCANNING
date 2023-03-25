#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
    char *vehicles[] = {"boat", "car", "truck", "train"};
    
    //prompt the user for the index of a vehicle and return that vehicle
    //-tabnine next line-
    int index = 0;
    printf("Enter the index of the vehicle you want: ");
    scanf("%d", &index);
    
    if (index >= 0 && index < 4) {
        printf("Vehicle %d is %s\n", index, vehicles[index]);
    } else {
        printf("Invalid index\n");
    }
    
    return 0;

    
    
}