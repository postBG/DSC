/* Description
 * Write a function to return an natural number in base 4
 */

#include <stdio.h>
#include <stdlib.h>
	
int base_four(int n){
/* Please write your code below */

	return 0;

}
/* Do not modify below */

void main(int argc, char* argv[]){

	if (argc != 2){
		printf("Enter any natural number n\n");
	}

	int n = atoi(argv[1]);		

	if (n < 0){
		printf("No negative number is allowed\n");
	}

	int f = 0;

	f = base_four(n);
	printf("%d\n",f);	
}

