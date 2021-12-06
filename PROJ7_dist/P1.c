#include <stdio.h>
#include <stdlib.h>

/* Linked list node structure */
struct Node {
    int data;
    struct Node* next;
};

/* Create a new node */
struct Node * createNode(struct Node * newNode, int data){
  newNode = (struct Node *) malloc(sizeof(struct Node));
  newNode->data = data;
  return newNode;
}


int main(int argc, char* argv[])
{  
  int length = argc - 1;

  /* Create a linked list from input integers */
  int k = 1;
  struct Node * head = NULL;
  struct Node * prev = NULL;
  struct Node * curr = NULL;

addNode:
  curr = createNode(curr, atoi(argv[k]));  
    
  if (k > 1)
    prev->next = curr;
  else
    head = curr;

  k++;
  prev = curr;

  if (k <= length)
    goto addNode;

  curr->next = NULL;

  /* Write your code here */	




	/* Do not modify below */	


  /* Pinrt reversed linked list */
  curr = head;
 
  while (curr){
    printf("%d", curr->data);
    curr = curr->next;
  }

  return 0;


}


