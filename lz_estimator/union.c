#include<stdio.h>
#include<stdlib.h>

struct Node
{
	int data;
	struct Node* next;

};

void insert(struct Node **head,int data)
{
	struct Node *newnode=(struct Node*)malloc(sizeof(struct Node));
	newnode->data=data;
	struct Node *current;

	struct Node *prev=NULL;
	if(*head==NULL)
	{
		*head=newnode;
		(*head)->next=NULL;
	}
	else
	{
		current=*head;
		while(current!=NULL)
		{
			prev=current;
			current=current->next;			
		}
		prev->next=newnode;
	}	
}

void printlist(struct Node **head)
{
	struct Node *temp=*head;
	while(temp!=NULL)
			{
				printf("%d=>",temp->data);
				temp=temp->next;
			}	
	printf("\n");		

}

struct Node* union_1(struct Node **head1,struct Node **head2)
{
	struct Node *temp1=*head1;
	struct Node *temp2=*head2;
	struct Node *head3=NULL;
	while((temp1!=NULL)||(temp2!=NULL))
	{
		if(temp1==NULL)
		{
			while(temp2!=NULL)
			{
				insert(&head3,temp2->data);
				temp2=temp2->next;
			}			
		}
		else if(temp2==NULL)
		{
			while(temp1!=NULL)
			{
				insert(&head3,temp1->data);
				temp1=temp1->next;
			}
		}
		else
		{
			if(temp1->data==temp2->data)
			{
				insert(&head3,temp1->data);
				temp1=temp1->next;
				temp2=temp2->next;
			}
			else if(temp1->data>temp2->data)
			{
				insert(&head3,temp1->data);
				temp1=temp1->next;
			}
			else
			{
				insert(&head3,temp2->data);
				temp2=temp2->next;
			}
		}
	
	}
	printlist(&head3);
	return(head3);

}
int main()
{
	struct Node* head1=NULL;
	struct Node* head2=NULL;
	struct Node* head3=NULL;
	int choice,num;
	while(1)
	{
		printf("1 to Enter in the first list\n2 to enter in second list\n");
		printf("3 to perform union\n4 to display lists\n");
		scanf("%d",&choice);
		switch(choice)
		{
			case 1:
			printf("enter number to be added to list 1\n");
			scanf("%d",&num);
			insert(&head1,num);
			break;

			case 2:
			printf("enter number to be added to list 2\n");
			scanf("%d",&num);
			insert(&head2,num);
			break;
			case 3:
			head3=union_1(&head1,&head2);
			break;
			case 4:
			printf("list1\n");
			printlist(&head1);
			printf("list2\n");
			printlist(&head2);
			printf("union\n");
			printlist(&head3);
			break;
			default:

			return 0;
		}
	}

	return 0;
}