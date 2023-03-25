#include <stdio.h>
#include <stdlib.h>

extern int getMonthlySales(int month);

int main(int argc, char *argv[]) {
    
    //sum the number of sales for the first quarter
    //-tabnine next line-
    int sum = 0;
    for (int i = 1; i <= 12; i++) {
        sum += getMonthlySales(i);
    }
    
    printf("%d\n", sum);
    
    return 0;
    

}