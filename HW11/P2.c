/* Description
 * Write a program that reads any english alphabet from the keyboard 
   and prints every character from that character down 
   to the character A in the order in which they appear in the ASCII table
 */

#include <stdio.h>

void main(int argc, char* argv[]){
	char c;
    printf("Enter any alphabet:");
    scanf("%c", &c);

    int counter;
    for (counter = c; counter >= 'A'; counter--){
        printf("%c", counter);
    }
}

