#include "lists.h"

/**
 * check_cycle - a function that checks for a cycle
 * @list: a pointer to a list
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *first, *second;

	if (list == NULL)
		return (0);
	first = list;
	second = list;
	while (first->next != NULL && second->next->next != NULL)
	{
		first = first->next;
		second = second->next->next;
		if (first == second)
			return (1);
	}
	return (0);
}
