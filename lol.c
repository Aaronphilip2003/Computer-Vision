// Online C compiler to run C program online
#include <stdio.h>

int main()
{
    int i,j,k;
    int a[5]={0,1,2,3,4};
    i=++a[0];
    j=a[1]++;
    printf("%d %d \n",i,j);
    printf("%d",j);
    return 0;

}