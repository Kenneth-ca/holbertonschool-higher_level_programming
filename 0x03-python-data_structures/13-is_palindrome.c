#include <stdio.h>
#include "lists.h"
/**
 * is_palindrome - a function that checks for palindrome
 * @head: the list
 *
 * Return: 0 if it is not a palindrome, 1 if it is
 */
int is_palindrome(listint_t **head)
{
	listint_t *temp;
    int length = 0;
    char buffer[10000];

	if (*head == NULL)
		return (0);
	temp = *head;
	while (temp != NULL)
	{
        length++;
        buffer[length] = temp->n;
		temp = temp->next;
	}
    printf("%s", buffer);
	return (1);
}
